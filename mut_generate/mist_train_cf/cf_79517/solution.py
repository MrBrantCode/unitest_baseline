"""
QUESTION:
Create a function `convert_timezone` that takes three parameters: a datetime object `original_time`, a string representing the original timezone `original_zone`, and a string representing the target timezone `target_zone`. The function should convert `original_time` from `original_zone` to `target_zone`, handling daylight saving changes. It should also handle exceptions where `original_zone` or `target_zone` is invalid, or where `original_time` is not a valid datetime object. Return the converted datetime object or an error message.
"""

from datetime import datetime
from pytz import timezone, UnknownTimeZoneError

def convert_timezone(original_time, original_zone, target_zone):
    try:
        # Create timezone objects
        original_tz = timezone(original_zone)
        target_tz = timezone(target_zone)

        # Localize the original time to the original timezone
        original_time = original_tz.localize(original_time)

        # Convert to the target timezone
        target_time = original_time.astimezone(target_tz)

        return target_time

    except UnknownTimeZoneError as e:
        print(f"Invalid timezone: {e}")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None