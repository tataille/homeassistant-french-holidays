"""UI configuration: defaults requested by Jean-Marc."""
import voluptuous as vol
from homeassistant import config_entries
from homeassistant.helpers.selector import SelectSelector, SelectSelectorConfig
from .const import DOMAIN, ACADEMIES, REGIONS, DEFAULT_ACADEMY, DEFAULT_REGION

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
        if user_input is not None:
            await self.async_set_unique_id(f"{user_input['academy']}:{user_input['region']}")
            self._abort_if_unique_id_configured()
            return self.async_create_entry(
                title=f"{user_input['academy']} · {REGION_LABELS[user_input['region']]}",
                data=user_input,
            )
        return self.async_show_form(step_id="user", data_schema=vol.Schema({
            vol.Required("academy", default=DEFAULT_ACADEMY): vol.In(ACADEMIES),
            vol.Required("region", default=DEFAULT_REGION): SelectSelector(
                SelectSelectorConfig(options=REGIONS, translation_key="region")
            ),
        }))
