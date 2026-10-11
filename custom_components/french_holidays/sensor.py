from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from .entity import FrenchHolidaysEntity

ENTITIES = {"next_public_holiday": "Next public holiday", "next_public_holiday_date": "Next public holiday date", "days_until_school_holidays": "Days until school holidays", "school_holiday_name": "School holiday name"}

async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities(FrenchHolidaysSensor(entry.runtime_data, key, label) for key, label in ENTITIES.items())

class FrenchHolidaysSensor(FrenchHolidaysEntity, SensorEntity):
    def __init__(self, coordinator, key, label):
        super().__init__(coordinator, key, label)
        if key == "next_public_holiday_date":
            self._attr_device_class = SensorDeviceClass.DATE
        if key == "days_until_school_holidays":
            self._attr_native_unit_of_measurement = "d"

    @property
    def native_value(self):
        return self.coordinator.data.get(self.key)
