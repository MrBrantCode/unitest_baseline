"""
QUESTION:
Write a function called `parse_timestamp` that takes two parameters: `timestamp` and `timezone`. 

The `timestamp` parameter should be a string in the format "YYYY-MM-DD HH:MM:SS" and may contain microseconds, indicated by a decimal point followed by up to 6 digits.

The `timezone` parameter should be a string representing the time zone.

The function should return a datetime object representing the given timestamp in the specified time zone.

The function should be able to handle a large number of timestamp inputs efficiently, parsing and converting at least 10,000 timestamp strings per second without significant performance degradation.
"""

from datetime import datetime
import pytz

def parse_timestamp(timestamp, timezone):
    tz = pytz.timezone(timezone)
    return datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S.%f").replace(tzinfo=tz)