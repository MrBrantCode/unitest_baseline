"""
QUESTION:
Get n seconds before the target time. See Example Test Cases about the format.
"""

from datetime import datetime, timedelta

def get_time_before_seconds(target_time: str, n: int) -> str:
    """
    Get the time n seconds before the target time.

    Parameters:
    - target_time (str): The target time in the format 'YYYY-MM-DD HH:MM:SS'.
    - n (int): The number of seconds to subtract from the target time.

    Returns:
    - str: The resulting time after subtracting n seconds from the target time, in the same format 'YYYY-MM-DD HH:MM:SS'.
    """
    target_datetime = datetime.strptime(target_time, '%Y-%m-%d %H:%M:%S')
    result_datetime = target_datetime - timedelta(seconds=n)
    return result_datetime.strftime('%Y-%m-%d %H:%M:%S')