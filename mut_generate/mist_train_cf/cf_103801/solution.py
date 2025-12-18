"""
QUESTION:
Create a function `convert_to_unix_timestamp` that takes a date string, a date format, and a timezone. The function should convert the date string to a UNIX timestamp in the given timezone. The date format and timezone will be provided. The function should return an integer representing the UNIX timestamp.
"""

import datetime
from dateutil import tz

def convert_to_unix_timestamp(date_string, date_format, timezone):
    """
    Convert a date string to a UNIX timestamp in a given timezone.

    Args:
        date_string (str): The date string to convert.
        date_format (str): The format of the date string.
        timezone (str): The timezone for the date string.

    Returns:
        int: The UNIX timestamp.
    """
    # Get the timezone object
    tz_obj = tz.gettz(timezone)

    # Convert the date string to a datetime object in the given timezone
    dt = datetime.datetime.strptime(date_string, date_format).replace(tzinfo=tz_obj)

    # Convert the datetime object to a UNIX timestamp
    unix_timestamp = int(dt.timestamp())

    return unix_timestamp