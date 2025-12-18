"""
QUESTION:
Create a function `valid_time` that takes a string representing time in the format "hh:mm" and returns `True` if the time is valid and `False` otherwise. A valid time satisfies the following conditions:
- The time string is not empty.
- The hours are between 0 and 23 (inclusive).
- The minutes are between 0 and 59 (inclusive).
- The time string is in the format "hh:mm" exactly.
"""

def valid_time(time: str) -> bool:
    if not time or len(time) != 5 or time[2] != ':':
        return False
    hours, minutes = time.split(':')
    if not hours.isdigit() or not minutes.isdigit():
        return False
    hours, minutes = int(hours), int(minutes)
    return 0 <= hours <= 23 and 0 <= minutes <= 59