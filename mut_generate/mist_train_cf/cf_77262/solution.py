"""
QUESTION:
Create a function `get_day_of_week(date)` that takes a string `date` in the format DDMMYYYY and returns the corresponding day of the week. The function should include validation checks for leap years and invalid dates, and the output should be the full day of the week (e.g., Wednesday). The input date string must be exactly 8 characters long. If the date is invalid, the function should return a corresponding error message.
"""

import datetime

def get_day_of_week(date):
    if len(date) != 8:
        return 'Invalid date format. It should be in DDMMYYYY format.'
    day = int(date[:2])
    month = int(date[2:4])
    year = int(date[4:])
    
    try:
        dt = datetime.datetime(year, month, day)
        return dt.strftime('%A')
    except ValueError as e:
        return str(e)