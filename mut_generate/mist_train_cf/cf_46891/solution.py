"""
QUESTION:
Create a function named `convert_timezone` that takes three parameters: `time_string`, `from_zone`, and `to_zone`. This function should convert a given time from the `from_zone` time zone to the `to_zone` time zone, handling Daylight Saving Time (DST) changes and different date and time formats. The function should return the converted time. The input time string should be in the format `%Y-%m-%d %H:%M:%S`. The function should also handle exceptions for invalid time, date, or timezone inputs.
"""

from datetime import datetime
from pytz import timezone

def convert_timezone(time_string, from_zone, to_zone):
    from_tz = timezone(from_zone)
    to_tz = timezone(to_zone)

    original_time = datetime.strptime(time_string, "%Y-%m-%d %H:%M:%S")

    # Localize the time to the from_zone timezone
    localized_time = from_tz.localize(original_time)

    # Convert the time to the to_zone timezone
    converted_time = localized_time.astimezone(to_tz)
    
    return converted_time