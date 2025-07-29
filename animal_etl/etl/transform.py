from dateutil import parser
import pytz

def transform_animal(animal):
    transformed = animal.copy()

    friends = transformed.get("friends", "")
    cleaned_friends = []
    for f in friends.split(","):
        f = f.strip()
        if f:
            cleaned_friends.append(f)
    transformed["friends"] = cleaned_friends

    born_at = transformed["born_at"]
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