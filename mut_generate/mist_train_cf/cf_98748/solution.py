"""
QUESTION:
Write a function called `convert_date` that takes a date string in mm/dd/yyyy format as input and converts it to dd-mm-yyyy format if the year is a leap year according to the Gregorian calendar. If the year is not a leap year, return an error message. The function should return the converted date in both numerical and textual format along with the day of the week on which the converted date falls.
"""

import datetime

def convert_date(date_string):
    date_obj = datetime.datetime.strptime(date_string, '%m/%d/%Y')
    if date_obj.year % 4 == 0 and (date_obj.year % 100 != 0 or date_obj.year % 400 == 0):
        converted_date_string = date_obj.strftime('%d-%m-%Y')
        day_of_week = date_obj.strftime('%A')
        month_name = date_obj.strftime('%B')
        return converted_date_string, month_name + ' ' + str(date_obj.year), day_of_week
    else:
        return 'Error: The year {} is not a leap year.'.format(date_obj.year)