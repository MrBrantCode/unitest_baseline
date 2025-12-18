"""
QUESTION:
Create a function named `day_of_week` that takes a date string in the format 'YYYY-MM-DD' as input, and returns the day of the week for the given date. The function should handle invalid date inputs and return an error message if the input date string does not comply with the correct format or is an invalid date.
"""

from datetime import datetime

def day_of_week(date):
    try:
        dt = datetime.strptime(date, '%Y-%m-%d')
        return dt.strftime('%A')
    except ValueError:
        return 'Invalid date. Please use the correct format (YYYY-MM-DD) and a valid date.'