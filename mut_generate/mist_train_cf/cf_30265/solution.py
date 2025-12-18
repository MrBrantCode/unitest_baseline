"""
QUESTION:
Implement the `timezone()` function, which takes a `datetime` object `date_time` in UTC timezone and a string `new_timezone` representing the new timezone. The function should return the `date_time` object converted to the specified `new_timezone`. Use the `pytz` library to manipulate timezones and handle the conversion.
"""

from pytz import timezone as tz

def timezone(date_time, new_timezone):
    # Convert the input date_time to UTC timezone
    utc_date_time = date_time.astimezone(tz('UTC'))

    # Convert the UTC date_time to the new timezone
    new_date_time = utc_date_time.astimezone(tz(new_timezone))

    return new_date_time