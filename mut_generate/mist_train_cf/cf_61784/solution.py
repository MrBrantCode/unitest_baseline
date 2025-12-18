"""
QUESTION:
Write a function named `convert_day_to_date` that takes two parameters: `year` (an integer between 1900 and 2100) and `day` (an integer between 1 and 366). The function should return a string representing the corresponding date in the format 'DD-MMM-YYYY', taking into account leap years.
"""

import datetime

def convert_day_to_date(year, day):
    date = datetime.datetime(year, 1, 1) + datetime.timedelta(day - 1)
    return date.strftime('%d-%b-%Y')