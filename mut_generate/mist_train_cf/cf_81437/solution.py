"""
QUESTION:
Write a function named `convert_time_to_awst` that takes a string representing time in 'HH:MM' format and converts it to Australian Western Standard Time (AWST) from Pacific Standard Time (PST), considering daylight saving time. The function should return the converted time as a string in 'HH:MM' format. The solution should use the `pytz` library, with 'America/Los_Angeles' for PST and 'Australia/Perth' for AWST time zones.
"""

from datetime import datetime
from pytz import timezone

def convert_time_to_awst(time_str):
    """
    Converts time from Pacific Standard Time (PST) to Australian Western Standard Time (AWST).

    Args:
    time_str (str): Time in 'HH:MM' format.

    Returns:
    str: Converted time in 'HH:MM' format.
    """
    pst = timezone('America/Los_Angeles')
    pst_time = pst.localize(datetime.strptime(time_str, '%H:%M'))
    awst = timezone('Australia/Perth')
    awst_time = pst_time.astimezone(awst)
    return awst_time.strftime('%H:%M')