"""Daily remote refresh, local midnight recalculation and persistent cache."""
import asyncio
import logging
from datetime import timedelta
from aiohttp import ClientError
from homeassistant.helpers.aiohttp_client import async_get_clientsession
from homeassistant.helpers.event import async_track_time_change
from homeassistant.helpers.storage import Store
from homeassistant.helpers.update_coordinator import DataUpdateCoordinator, UpdateFailed
from homeassistant.util import dt as dt_util
from .const import DOMAIN, VERSION
from .engine import normalize_school, validate_public, states

_LOGGER = logging.getLogger(__name__)
SCHOOL_URL = "https://data.education.gouv.fr/api/explore/v2.1/catalog/datasets/fr-en-calendrier-scolaire/records"

class FrenchHolidaysCoordinator(DataUpdateCoordinator):
    def __init__(self, hass, entry):
        super().__init__(hass, _LOGGER, name=DOMAIN, config_entry=entry, update_interval=timedelta(hours=1))
        self.entry = entry
        self.public = {}
        self.school = []
        self.updated = None
        self.stale = False
        self.store = Store(hass, 1, f"{DOMAIN}.{entry.entry_id}")
        entry.async_on_unload(async_track_time_change(hass, self._midnight, hour=0, minute=0, second=0))

    def calendar_states(self):
        return states(dt_util.now().date(), self.public, self.school,
                      academy=self.entry.data["academy"],
                      region=self.entry.data["region"], version=VERSION)

    async def async_load_cache(self):
        cached = await self.store.async_load()
        if cached:
            try:
                self.public = validate_public(cached["public"])
                self.school = cached["school"]
                self.updated = dt_util.parse_datetime(cached["updated"])
                if any("zone" not in event for event in self.school):
                    self.updated = None
                    return  # Refresh legacy caches to obtain school zones.
                if not self.school or self.updated is None:
                    raise ValueError("Invalid cache")
            except (ValueError, KeyError, TypeError):
                self.public, self.school, self.updated = {}, [], None

    async def _midnight(self, now):
        if self.public and self.school:
            self.async_set_updated_data(self.calendar_states())
        await self.async_request_refresh()

    async def _get(self, url, params=None):
        session = async_get_clientsession(self.hass)
        async with asyncio.timeout(30):
            async with session.get(url, params=params) as response:
                response.raise_for_status()
                return await response.json()

    async def _fetch_school(self):
        records = []
        offset = 0
        while True:
            payload = await self._get(SCHOOL_URL, {
                "where": f'location="{self.entry.data["academy"]}"',
                "order_by": "start_date", "limit": 100, "offset": offset,
            })
            batch = payload["results"]
            records.extend(batch)
            offset += len(batch)
            if offset >= payload["total_count"]:
                break
            if not batch or offset >= 10000:
                raise ValueError("Incomplete school calendar")
        return normalize_school(records)

    async def _async_update_data(self):
        now = dt_util.utcnow()
        if self.updated is None or now - self.updated >= timedelta(days=1):
            try:
                public, school = await asyncio.gather(
                    self._get(f'https://calendrier.api.gouv.fr/jours-feries/{self.entry.data["region"]}.json'),
                    self._fetch_school(),
                )
                self.public, self.school = validate_public(public), school
                self.updated = now
                self.stale = False
                await self.store.async_save({"public": self.public, "school": self.school, "updated": now.isoformat()})
            except (ClientError, TimeoutError, ValueError, KeyError, TypeError) as err:
                if not self.public or not self.school:
                    raise UpdateFailed(f"Official calendars unavailable: {err}") from err
                self.stale = True
                _LOGGER.warning("Official calendars unavailable; using cached data: %s", err)
        return self.calendar_states()
