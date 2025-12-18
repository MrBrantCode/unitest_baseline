"""
QUESTION:
Create a function `interpret_date` that takes a date string in 'MM-DD-YYYY' format and returns a string representing the date in 'Month Day, Year' format. The function should interpret numerical months and format the output accordingly.
"""

from datetime import datetime

def interpret_date(date_string):
    date_obj = datetime.strptime(date_string, '%m-%d-%Y')

    month = date_obj.strftime('%B')
    day = date_obj.strftime('%d')
    year = date_obj.strftime('%Y')

    return "{} {}, {}".format(month, day, year)