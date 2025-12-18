"""
QUESTION:
Write a function named 'convert_leap_year_date' that takes a date string in 'mm/dd/yyyy' format as input and returns a string representing the date in 'dd-mm-yyyy' format if the year is a leap year according to the Gregorian calendar, along with the day of the week. If the year is not a leap year, return an error message.
"""

import datetime

def convert_leap_year_date(date_string):
    date_obj = datetime.datetime.strptime(date_string, '%m/%d/%Y')
    if date_obj.year % 4 == 0 and (date_obj.year % 100 != 0 or date_obj.year % 400 == 0):
        converted_date_string = date_obj.strftime('%d-%m-%Y')
        day_of_week = date_obj.strftime('%A')
        return f'{converted_date_string} {day_of_week}'
    else:
        return f'Error: The year {date_obj.year} is not a leap year.'