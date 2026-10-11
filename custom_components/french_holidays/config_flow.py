"""UI configuration: defaults requested by Jean-Marc."""
import voluptuous as vol
from homeassistant import config_entries
from .const import DOMAIN, ACADEMIES, REGIONS, DEFAULT_ACADEMY, DEFAULT_REGION

class FrenchHolidaysConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        if user_input is not None:
            await self.async_set_unique_id(f"{user_input['academy']}:{user_input['region']}")
            self._abort_if_unique_id_configured()
            return self.async_create_entry(title=f"French Holidays · {user_input['academy']} / {user_input['region']}", data=user_input)
        return self.async_show_form(step_id="user", data_schema=vol.Schema({
            vol.Required("academy", default=DEFAULT_ACADEMY): vol.In(ACADEMIES),
            vol.Required("region", default=DEFAULT_REGION): vol.In(REGIONS),
        }))
