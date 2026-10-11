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
        }[key]
        self._attr_device_info = DeviceInfo(identifiers={(DOMAIN, coordinator.entry.entry_id)}, name=f"French Holidays {coordinator.entry.data['academy']} {coordinator.entry.data['region']}", manufacturer="French Holidays", model="Official calendars")

    @property
    def extra_state_attributes(self):
        return {"academy": self.coordinator.entry.data["academy"], "region": self.coordinator.entry.data["region"], "cached_data": self.coordinator.stale, "last_remote_update": self.coordinator.updated.isoformat() if self.coordinator.updated else None}
