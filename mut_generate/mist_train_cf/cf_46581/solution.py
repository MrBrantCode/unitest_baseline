"""
QUESTION:
Write a function `date_to_weekday(date)` that takes an 8-digit string representing a date in the format DDMMYYYY, where DD is the day, MM is the month, and YYYY is the year. The function should return the weekday (in words, e.g., "Monday", "Tuesday", etc.) corresponding to the provided date in the Gregorian calendar.
"""

from datetime import datetime

def date_to_weekday(date):
    # Parse date
    day = int(date[0:2])
    month = int(date[2:4])
    year = int(date[4:8])

    # Create date object
    date = datetime(year, month, day)

    # Weekday names
    days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Return corresponding weekday
    return days[date.weekday()]