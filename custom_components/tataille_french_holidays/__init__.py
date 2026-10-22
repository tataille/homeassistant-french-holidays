"""French Holidays integration."""
from homeassistant.const import Platform
from .coordinator import FrenchHolidaysCoordinator

PLATFORMS = [Platform.BINARY_SENSOR, Platform.SENSOR]

async def async_setup_entry(hass, entry):
    coordinator = FrenchHolidaysCoordinator(hass, entry)
    await coordinator.async_load_cache()
    await coordinator.async_config_entry_first_refresh()
    entry.runtime_data = coordinator
    await hass.config_entries.async_forward_entry_setups(entry, PLATFORMS)
    return True

async def async_unload_entry(hass, entry):
    return await hass.config_entries.async_unload_platforms(entry, PLATFORMS)
