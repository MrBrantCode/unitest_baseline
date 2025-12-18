"""
QUESTION:
Write a function `calculate_time_difference` that calculates the difference between two times given in 24-hour format. The function should handle cases where the times cross over midnight, invalid time inputs, and incorrect sorting of the two times. The function should return the time difference in the format "X days, HH:MM:SS" or "HH:MM:SS" if less than a day. If the input times are invalid, return "Invalid Time Format".
"""

from datetime import datetime, timedelta

def calculate_time_difference(time1: str, time2: str) -> str:
    time_format = "%H:%M:%S"
    try:
        datetime1 = datetime.strptime(time1, time_format)
        datetime2 = datetime.strptime(time2, time_format)
        if datetime2 >= datetime1:
            time_diff = datetime2 - datetime1
        else:  # for cases where we cross midnight
            datetime2 += timedelta(days=1)
            time_diff = datetime2 - datetime1
        days = time_diff.days
        hours, remainder = divmod(time_diff.seconds, 3600)
        minutes, seconds = divmod(remainder, 60)
        if days > 0:
            return f"{days} days, {hours:02}:{minutes:02}:{seconds:02}"
        else:
            return f"{hours:02}:{minutes:02}:{seconds:02}"
    except ValueError:
        return "Invalid Time Format"