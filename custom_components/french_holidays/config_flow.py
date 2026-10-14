"""UI configuration for French holidays."""
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers.selector import SelectSelector, SelectSelectorConfig

from .const import ACADEMIES, DOMAIN, REGIONS


REGION_LABELS = {
    "metropole": "France métropolitaine",
    "alsace-moselle": "Alsace-Moselle",
    "guadeloupe": "Guadeloupe",
    "martinique": "Martinique",
    "guyane": "Guyane",
    "la-reunion": "La Réunion",
    "mayotte": "Mayotte",
}


class FrenchHolidaysConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    async def async_step_user(self, user_input=None):
        errors = {}

        if user_input is not None:
            academy = user_input.get("academy")
            region = user_input.get("region")

            if (
                not isinstance(academy, str)
                or not academy.strip()
                or academy not in ACADEMIES
                or not isinstance(region, str)
                or not region.strip()
                or region not in REGIONS
            ):
                errors["base"] = "invalid_selection"
            else:
                await self.async_set_unique_id(f"{academy}:{region}")
                self._abort_if_unique_id_configured()
                return self.async_create_entry(
                    title=f"{academy} · {REGION_LABELS[region]}",
                    data=user_input,
                )

        return self.async_show_form(
            step_id="user",
            data_schema=vol.Schema(
                {
                    vol.Required("academy"): vol.In(ACADEMIES),
                    vol.Required("region"): SelectSelector(
                        SelectSelectorConfig(
                            options=REGIONS,
                            translation_key="region",
                        )
                    ),
                }
            ),
            errors=errors,
        )
