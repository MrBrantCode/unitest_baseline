"""
QUESTION:
Write a function named `convert_time` that takes the time in Central European Time (CET) and converts it to the corresponding time in the time zone UTC+5, considering the standard 4-hour difference. The input time is in 24-hour format.
"""

def convert_time(cet_time):
    """
    Converts the time in Central European Time (CET) to the corresponding time in UTC+5.

    Args:
        cet_time (str): The time in CET in 24-hour format (HH:MM).

    Returns:
        str: The corresponding time in UTC+5 in 24-hour format (HH:MM).
    """
    hours, minutes = map(int, cet_time.split(':'))
    utc_plus_5_hours = (hours + 4) % 24
    return f"{utc_plus_5_hours:02d}:{minutes:02d}"