"""
QUESTION:
Create a function named `convert_CET_to_UTC` that takes two parameters: `cet_time` (a datetime object representing time in Central European Time) and `utc_offset` (an integer representing the desired UTC offset). The function should return the time in UTC format with the specified offset, taking into account daylight saving time adjustments.
"""

from datetime import datetime, timedelta
import pytz

def convert_CET_to_UTC(cet_time, utc_offset):
    # Define timezone for CET
    cet = pytz.timezone('CET')

    # localize inputted time to CET
    cet_time = cet.localize(cet_time)

    # Convert CET time to UTC
    utc_time = cet_time.astimezone(pytz.UTC)

    # Calculating the required UTC offset
    desired_utc_time = utc_time - timedelta(hours=utc_offset)
    
    return desired_utc_time