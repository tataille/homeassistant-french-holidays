"""Pure calendar logic. School dates use the French civil calendar."""
from datetime import date, datetime, timedelta
from zoneinfo import ZoneInfo

PARIS = ZoneInfo("Europe/Paris")

def school_date(value):
    return datetime.fromisoformat(value.replace("Z", "+00:00")).astimezone(PARIS).date()

def normalize_school(records):
    events = set()
    for row in records:
        if row.get("population") not in (None, "-", "Élèves", "Elèves", "élèves"):
            continue
        start, end = school_date(row["start_date"]), school_date(row["end_date"])
        if end > start:
            events.add((start.isoformat(), end.isoformat(), row["description"], row.get("zones") or ""))
    if not events:
        raise ValueError("No school holiday records for this academy")
    return [dict(start=s, end=e, name=n, zone=z or None) for s, e, n, z in sorted(events)]

def validate_public(payload):
    if not isinstance(payload, dict) or not payload:
        raise ValueError("Empty public holiday data")
    for day, name in payload.items():
        date.fromisoformat(day)
        if not isinstance(name, str) or not name:
            raise ValueError("Invalid holiday name")
    return payload

def states(today, public, school, *, academy=None, region=None, version=None):
    tomorrow = today + timedelta(days=1)
    current = next((e for e in school if e["start"] <= today.isoformat() < e["end"]), None)
    following = next((e for e in school if e["start"] > today.isoformat()), None)
    next_public = next(((d,n) for d,n in sorted(public.items()) if d > today.isoformat()), None)
    school_known = bool(school) and min(e["start"] for e in school) <= today.isoformat() < max(e["end"] for e in school)
    public_known = any(d.startswith(str(today.year)+"-") for d in public)
    beginning_year = today.year if today.month >= 9 else today.year - 1
    zone_event = current or following or (school[-1] if school else {})
    return {
        "day": (today.weekday() + 1) % 7,
        "year": today.year,
        "school_period": f"{beginning_year}-{beginning_year + 1}",
        "academy": academy,
        "region": region,
        "zones": zone_event.get("zone"),
        "version": version,
        "public_holiday_name": public.get(today.isoformat()),
        "school_holidays_end_date": date.fromisoformat(current["end"]) if current else None,
        "next_school_holidays": following["name"] if following else None,
        "next_school_holidays_start": date.fromisoformat(following["start"]) if following else None,
        "next_school_holidays_end": date.fromisoformat(following["end"]) if following else None,
        "next_school_holidays_countdown": (date.fromisoformat(following["start"])-today).days if following else None,
        "public_holiday": today.isoformat() in public if public_known else None,
        "public_holiday_tomorrow": tomorrow.isoformat() in public if any(d.startswith(str(tomorrow.year)+"-") for d in public) else None,
        "school_holidays": current is not None if school_known else None,
        "school_holidays_tomorrow": any(e["start"] <= tomorrow.isoformat() < e["end"] for e in school) if school_known and tomorrow.isoformat() < max(e["end"] for e in school) else None,
        "next_public_holiday": next_public[1] if next_public else None,
        "next_public_holiday_date": date.fromisoformat(next_public[0]) if next_public else None,
        "days_until_school_holidays": 0 if current else (date.fromisoformat(following["start"])-today).days if following else None,
        "school_holiday_name": current["name"] if current else None,
        "weekend": today.weekday() >= 5,
        "working_day": today.weekday() < 5 and today.isoformat() not in public if public_known else None,
    }
