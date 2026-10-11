from homeassistant.helpers.entity import EntityCategory
from homeassistant.components.sensor import SensorEntity, SensorDeviceClass
from .entity import FrenchHolidaysEntity

ENTITIES = {'next_public_holiday': 'Next public holiday', 'next_public_holiday_date': 'Next public holiday date', 'days_until_school_holidays': 'Days until school holidays', 'school_holiday_name': 'School holiday name', 'public_holiday_name': 'Public holiday name', 'school_holidays_end_date': 'School holidays end date', 'next_school_holidays': 'Next school holidays', 'next_school_holidays_start': 'Next school holidays start', 'next_school_holidays_end': 'Next school holidays end', 'next_school_holidays_countdown': 'Next school holidays countdown', 'day': 'Day of week', 'year': 'Year', 'school_period': 'School year', 'academy': 'Academy', 'region': 'Public holiday region', 'zones': 'School zone', 'version': 'Integration version'}

async def async_setup_entry(hass, entry, async_add_entities):
    async_add_entities(FrenchHolidaysSensor(entry.runtime_data, key, label) for key, label in ENTITIES.items())

class FrenchHolidaysSensor(FrenchHolidaysEntity, SensorEntity):
    def __init__(self, coordinator, key, label):
        super().__init__(coordinator, key, label)
        if key in {"next_public_holiday_date", "school_holidays_end_date", "next_school_holidays_start", "next_school_holidays_end"}:
            self._attr_device_class = SensorDeviceClass.DATE
        if key in {"days_until_school_holidays", "next_school_holidays_countdown"}:
            self._attr_native_unit_of_measurement = "d"

        if key in {"academy", "region", "zones", "version"}:
            self._attr_entity_category = EntityCategory.DIAGNOSTIC

    @property
    def native_value(self):
        return self.coordinator.data.get(self.key)
