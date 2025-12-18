"""
QUESTION:
Write a function named `convert_to_standard_format` that takes a string in the format 'YYYY-MM-DD HHMM' representing a date and time in military (24-hour) format and returns a string representing the same date and time in standard (12-hour) format, including the day of the week.
"""

from datetime import datetime

def convert_to_standard_format(date_time):
    datetime_obj = datetime.strptime(date_time, "%Y-%m-%d %H%M")
    standard_format = datetime_obj.strftime("%A, %I:%M %p on %B %d, %Y")
    return standard_format