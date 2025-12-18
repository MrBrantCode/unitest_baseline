"""
QUESTION:
Write a function named `get_current_time_with_offset` that takes a time zone string as input and returns the current date and time in the specified time zone with a 5-hour offset, formatted as "yyyy-MM-dd hh:mm:ss tt," while accounting for daylight saving time.
"""

import datetime
import pytz

def get_current_time_with_offset(timezone_name):
    # Get current date and time in the local time zone
    local_dt = datetime.datetime.now(datetime.timezone.utc).astimezone()

    # Convert local date and time to specified time zone
    timezone = pytz.timezone(timezone_name)
    dt = local_dt.astimezone(timezone)

    # Add 5-hour offset to converted date and time
    dt = dt + datetime.timedelta(hours=5)

    # Normalize date and time to account for future daylight saving changes
    dt = timezone.normalize(dt)

    # Format date and time string
    date_string = dt.strftime('%Y-%m-%d %I:%M:%S %p')

    return date_string