"""
QUESTION:
Write a function, which takes a non-negative integer (seconds) as input and returns the time in a human-readable format (`HH:MM:SS`)

* `HH` = hours, padded to 2 digits, range: 00 - 99
* `MM` = minutes, padded to 2 digits, range: 00 - 59
* `SS` = seconds, padded to 2 digits, range: 00 - 59

The maximum time never exceeds 359999 (`99:59:59`)

You can find some examples in the test fixtures.
"""

def convert_seconds_to_readable_time(seconds: int) -> str:
    """
    Converts a given number of seconds into a human-readable time format (HH:MM:SS).

    Parameters:
    - seconds (int): A non-negative integer representing the total number of seconds.

    Returns:
    - str: A string in the format 'HH:MM:SS', where HH is hours, MM is minutes, and SS is seconds.
    """
    hours = seconds // 3600
    minutes = (seconds // 60) % 60
    seconds = seconds % 60
    return f'{hours:02}:{minutes:02}:{seconds:02}'