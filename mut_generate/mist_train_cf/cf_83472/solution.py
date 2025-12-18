"""
QUESTION:
Write a function `weekday_from_date(day, month, year)` that takes the day, month, and year of a date as integers and returns a tuple containing the name of the weekday and the number of days until the next occurrence of the same weekday. The name of the weekday should be one of the following: "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday". The dates provided will always be valid and fall within the years 1971 and 2100.
"""

import datetime

def weekday_from_date(day, month, year):
    # Create a datetime object from day, month, year
    current_date = datetime.datetime(year, month, day)
    # Get the weekday of the date
    current_weekday = current_date.strftime('%A')
    # The next occurrence of the same weekday from any day is always after 7 days
    return (current_weekday, 7)