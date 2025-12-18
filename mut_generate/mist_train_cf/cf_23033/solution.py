"""
QUESTION:
Write a function `convert_to_local_time` that takes a date and time string in the format 'YYYY-MM-DDTHH:mm:ss.sssZ' and the user's local timezone offset in minutes as input. The function should return the date and time string converted to the user's local timezone in the same format. The function should not take into account any daylight saving time (DST) adjustments.
"""

from datetime import datetime
import pytz

def convert_to_local_time(date_string, offset_minutes):
    """
    Converts a date and time string in the format 'YYYY-MM-DDTHH:mm:ss.sssZ' to the user's local timezone.

    Args:
    date_string (str): Date and time string in the format 'YYYY-MM-DDTHH:mm:ss.sssZ'
    offset_minutes (int): User's local timezone offset in minutes

    Returns:
    str: Date and time string converted to the user's local timezone in the same format
    """

    # Parse the input date string
    date = datetime.strptime(date_string, '%Y-%m-%dT%H:%M:%S.%fZ')

    # Convert the date to UTC timezone
    utc_date = date.replace(tzinfo=pytz.UTC)

    # Calculate the user's local timezone offset
    offset = pytz.FixedOffset(offset_minutes // 60 * 60 + offset_minutes % 60)

    # Convert the date to the user's local timezone
    local_date = utc_date.astimezone(offset)

    # Format the local date back to the original string format
    local_date_string = local_date.strftime('%Y-%m-%dT%H:%M:%S.%f') + 'Z'

    return local_date_string