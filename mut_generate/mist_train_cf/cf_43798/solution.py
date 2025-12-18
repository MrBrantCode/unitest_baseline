"""
QUESTION:
Write a function `convert_unix_to_iso(timestamps, timezone='UTC')` that takes a list of Unix timestamps and an optional timezone string as input, and returns a list of ISO 8601 formatted timestamps. The function should handle edge cases involving invalid or incorrect inputs, including non-integer timestamps and unknown timezones. If a timezone is not provided, it defaults to 'UTC'.
"""

from datetime import datetime
import pytz

def convert_unix_to_iso(timestamps, timezone='UTC'):
    try:
        tz = pytz.timezone(timezone)
    except pytz.exceptions.UnknownTimeZoneError:
        return "Unknown Timezone Error"

    converted_times = []
    for timestamp in timestamps:
        try:
            dt = datetime.fromtimestamp(int(timestamp), tz)
            converted_times.append(dt.isoformat())
        except ValueError:
            converted_times.append('Invalid Timestamp Error')

    return converted_times