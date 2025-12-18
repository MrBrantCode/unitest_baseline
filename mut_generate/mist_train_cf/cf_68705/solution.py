"""
QUESTION:
Create a function called `convert_CET_to_UTC` that takes in two parameters: `cet_time` and `utc_offset`. `cet_time` is a datetime object representing the time in Central European Time (CET), and `utc_offset` is an integer representing the desired UTC offset. The function should return the converted time in UTC, taking into account daylight saving time (DST) adjustments.
"""

from datetime import datetime, timedelta
import pytz

def convert_CET_to_UTC(cet_time, utc_offset):
    """
    This function converts Central European Time (CET) to Coordinated Universal Time (UTC).

    Parameters:
    cet_time (datetime): The input time in CET
    utc_offset (int): The UTC offset

    Returns:
    datetime: Converted time in UTC
    """
    # Assuming `cet_time` is naive (i.e., unaware of time zone), let's first make it aware
    cet = pytz.timezone('CET')
    aware_cet_time = cet.localize(cet_time)

    # Now let's compute the correct offset
    correct_utc_offset = utc_offset-1 # Because CET is UTC+1

    # But we need to take DST into account
    if aware_cet_time.dst() != timedelta(0):
        # DST is in effect, timezone is CEST (UTC+2)
        correct_utc_offset = utc_offset - 2

    # Finally let's return the converted time
    return aware_cet_time + timedelta(hours=correct_utc_offset)