from dateutil import parser
import pytz
import time

def transform_animal(animal):
    transformed = animal.copy()

    friends = transformed.get("friends", "")
    cleaned_friends = []
    for f in friends.split(","):
        f = f.strip()
        if f:
            cleaned_friends.append(f)
    transformed["friends"] = cleaned_friends

    born_at = transformed.get("born_at")
    if born_at:
        try:
            dt = parser.parse(born_at)
            dt_utc = dt.astimezone(pytz.UTC)
            transformed["born_at"] = dt_utc.isoformat()
        except Exception:
            transformed["born_at"] = None
    else:
        transformed["born_at"] = None

    return transformed

def transform_animal_for_upload(animal):
    transformed = {
        "id": animal.get("id"),
        "name": animal.get("name"),
    }

    friends = animal.get("friends", "")
    if isinstance(friends, list):
        transformed["friends"] = ", ".join(friends)
    else:
        transformed["friends"] = str(friends).strip()

    born_at = animal.get("born_at")
    if born_at:
        try:
            dt = parser.parse(born_at)
            dt_utc = dt.astimezone(pytz.UTC)
            unix_ts = int(dt_utc.timestamp())
            transformed["born_at"] = unix_ts
        except Exception:
            pass

    return transformed
