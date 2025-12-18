"""
QUESTION:
Write a function `convert_date_format(us_date)` that takes a string representing a date in the format MM/DD/YYYY and returns the same date in the format DD-MM-YYYY. If the input string is not in the correct format, the function should return 'Invalid Date Format'.
"""

from datetime import datetime

def convert_date_format(us_date):
    try:
        real_date = datetime.strptime(us_date, '%m/%d/%Y')
        return real_date.strftime('%d-%m-%Y')
    except ValueError:
        return 'Invalid Date Format'