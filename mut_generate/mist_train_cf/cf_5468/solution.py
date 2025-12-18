"""
QUESTION:
Create a function `convert_to_date` that takes a string `date_string` in the format "dd-mm-yyyy" and returns a date object. The function should raise an error or return None if the input string is not in the correct format, or if the year is not in the range of 1900 to 2099, or if the month is not between 1 and 12.
"""

import datetime

def convert_to_date(date_string):
    try:
        date_obj = datetime.datetime.strptime(date_string, "%d-%m-%Y")
        if 1900 <= date_obj.year <= 2099 and 1 <= date_obj.month <= 12:
            return date_obj.date()
        else:
            return None
    except ValueError:
        return None