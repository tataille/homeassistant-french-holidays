from homeassistant.components.binary_sensor import BinarySensorEntity
from .entity import FrenchHolidaysEntity

ENTITIES = {"public_holiday": "Public holiday", "public_holiday_tomorrow": "Public holiday tomorrow", "school_holidays": "School holidays", "school_holidays_tomorrow": "School holidays tomorrow", "weekend": "Weekend", "working_day": "Working day"}

async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities(FrenchHolidaysBinarySensor(entry.runtime_data, key, label) for key, label in ENTITIES.items())

class FrenchHolidaysBinarySensor(FrenchHolidaysEntity, BinarySensorEntity):
    @property
    def is_on(self):
        return self.coordinator.data.get(self.key)
