"""
QUESTION:
Write a function called `get_day_of_week` that takes a date string in the format "Month Day, Year" (e.g., "June 3, 2020") and returns the corresponding day of the week as a string (e.g., "Monday", "Tuesday", etc.). The function should use the Python datetime module and return the day of the week for the given date.
"""

from datetime import datetime

def get_day_of_week(date):
    date_object = datetime.strptime(date, '%B %d, %Y')
    return date_object.strftime('%A')