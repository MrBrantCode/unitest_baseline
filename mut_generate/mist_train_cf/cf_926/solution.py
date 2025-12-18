"""
QUESTION:
Write a function called `convert_date_format()` that takes a string date in the format 'dd/mm/yyyy' and returns a string in the format 'yyyy/mm/dd'. The function should handle leap years and dates before the year 1900. If the input date is invalid, the function should return an error message.
"""

import datetime

def convert_date_format(date):
    day, month, year = date.split('/')
    if int(year) < 1900:
        return 'Invalid date format.'
    if int(month) < 1 or int(month) > 12:
        return 'Invalid date format.'
    if int(day) < 1 or int(day) > 31:
        return 'Invalid date format.'
    if int(month) in [4, 6, 9, 11] and int(day) > 30:
        return 'Invalid date format.'
    if int(month) == 2:
        if int(year) % 4 == 0:
            if int(year) % 100 == 0:
                if int(year) % 400 == 0:
                    if int(day) > 29:
                        return 'Invalid date format.'
                else:
                    if int(day) > 28:
                        return 'Invalid date format.'
            else:
                if int(day) > 29:
                    return 'Invalid date format.'
        else:
            if int(day) > 28:
                return 'Invalid date format.'
    return f'{year}/{month}/{day}'