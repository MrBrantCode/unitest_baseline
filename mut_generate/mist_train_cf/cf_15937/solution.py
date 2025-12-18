"""
QUESTION:
Write a function called `convert_date` that takes a date string in the format 'dd/mm/yyyy' and returns a date string in the format 'yyyy/mm/dd'. The function should account for leap years and handle dates before 1900, with the following restrictions:
- The year should be 1900 or later.
- The month should be between 1 and 12.
- The day should be within the valid range for the given month, taking into account leap years for February.
If the input date is invalid, the function should return an error message.
"""

import datetime

def convert_date(date):
    try:
        day, month, year = map(int, date.split('/'))
        if (year < 1900 or month < 1 or month > 12 or 
            (month == 2 and ((year % 4 != 0) or (year % 100 == 0 and year % 400 != 0)) and (day < 1 or day > 28)) or 
            (month in [4, 6, 9, 11] and (day < 1 or day > 30)) or 
            (day < 1 or day > 31)):
            return "Invalid date"
        else:
            converted_date = datetime.datetime(year, month, day).strftime('%Y/%m/%d')
            return converted_date
    except ValueError:
        return "Invalid date"