"""
QUESTION:
Implement a function called `convert_date_format` that takes a string date in the format MM/DD/YYYY as input and returns the date in the format DD-MM-YYYY, correctly handling leap years.
"""

from datetime import datetime

def convert_date_format(date_string):
    date = datetime.strptime(date_string, "%m/%d/%Y")
    converted_date = date.strftime("%d-%m-%Y")
    return converted_date