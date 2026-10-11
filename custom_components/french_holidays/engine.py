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
            events.add((start.isoformat(), end.isoformat(), row["description"]))
    if not events:
        raise ValueError("No school holiday records for this academy")
    return [dict(start=s, end=e, name=n) for s, e, n in sorted(events)]

def validate_public(payload):
    if not isinstance(payload, dict) or not payload:
        raise ValueError("Empty public holiday data")
    for day, name in payload.items():
        date.fromisoformat(day)
        if not isinstance(name, str) or not name:
            raise ValueError("Invalid holiday name")
    return payload

def states(today, public, school):
    tomorrow = today + timedelta(days=1)
    current = next((e for e in school if e["start"] <= today.isoformat() < e["end"]), None)
    following = next((e for e in school if e["start"] > today.isoformat()), None)
    next_public = next(((d,n) for d,n in sorted(public.items()) if d >= today.isoformat()), None)
    school_known = bool(school) and min(e["start"] for e in school) <= today.isoformat() < max(e["end"] for e in school)
    public_known = any(d.startswith(str(today.year)+"-") for d in public)
    return {
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
