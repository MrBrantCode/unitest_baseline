"""
QUESTION:
Implement the function `formatDateTime(date, time, format)` that takes a date string in the format "YYYY-MM-DD", a time string in the format "HH:MM:SS", and a format string as input, and returns the formatted date and time according to the given format string. The format string can contain the following placeholders: %d, %H, %I, %M, %S, %a, %A, %b, %B, %c, %j, %p, %U, and %w.
"""

from datetime import datetime

def formatDateTime(date, time, format):
    datetime_str = date + " " + time
    dt = datetime.strptime(datetime_str, "%Y-%m-%d %H:%M:%S")
    formatted_datetime = dt.strftime(format)
    return formatted_datetime