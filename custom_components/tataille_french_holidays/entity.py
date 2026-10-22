from homeassistant.helpers.entity import DeviceInfo
from homeassistant.helpers.update_coordinator import CoordinatorEntity
from .const import DOMAIN

class FrenchHolidaysEntity(CoordinatorEntity):
    _attr_has_entity_name = True

    def __init__(self, coordinator, key, label):
        super().__init__(coordinator)
        self.key = key
        self._attr_unique_id = f"{coordinator.entry.entry_id}_{key}"
        self._attr_translation_key = key
        self._attr_icon = {
            "public_holiday": "mdi:calendar-star",
            "public_holiday_tomorrow": "mdi:calendar-arrow-right",
            "school_holidays": "mdi:school",
            "school_holidays_tomorrow": "mdi:calendar-clock",
            "weekend": "mdi:calendar-weekend",
            "working_day": "mdi:briefcase-outline",
            "next_public_holiday": "mdi:calendar-star",
            "next_public_holiday_date": "mdi:calendar",
            "days_until_school_holidays": "mdi:calendar-clock",
            "school_holiday_name": "mdi:school-outline",
            'public_holiday_name': 'mdi:calendar-star',
            'school_holidays_end_date': 'mdi:calendar-end',
            'next_school_holidays': 'mdi:school-outline',
            'next_school_holidays_start': 'mdi:calendar-start',
            'next_school_holidays_end': 'mdi:calendar-end',
            'next_school_holidays_countdown': 'mdi:calendar-clock',
            'day': 'mdi:calendar-today',
            'year': 'mdi:calendar',
            'school_period': 'mdi:school',
            'academy': 'mdi:school-outline',
            'region': 'mdi:map-marker-outline',
            'zones': 'mdi:map-outline',
            'version': 'mdi:information-outline',
        }[key]
        self._attr_device_info = DeviceInfo(identifiers={(DOMAIN, coordinator.entry.entry_id)}, name=f"French Holidays {coordinator.entry.data['academy']} {coordinator.entry.data['region']}", manufacturer="French Holidays", model="Official calendars")

    @property
    def extra_state_attributes(self):
        attributes = {"academy": self.coordinator.entry.data["academy"], "region": self.coordinator.entry.data["region"], "cached_data": self.coordinator.stale, "last_remote_update": self.coordinator.updated.isoformat() if self.coordinator.updated else None}
        if self.key == "next_school_holidays_countdown":
            value = self.coordinator.data.get(self.key)
            attributes["nextSchoolHolidaysCountdownInDays"] = value
            attributes["nextSchoolHolidaysCoutdownInDays"] = value
        return attributes
