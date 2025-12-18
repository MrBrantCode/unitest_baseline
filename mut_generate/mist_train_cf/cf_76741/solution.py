"""
QUESTION:
Write a function `convert_date_string(date_string)` to convert a given date string into a datetime object. The date string is either in the format "%m/%d/%Y %H:%M:%S" or "%d/%m/%Y %H:%M:%S". If the date string does not match either format, the function should return None.
"""

import datetime

def convert_date_string(date_string):
    incorrect_date_format = "%m/%d/%Y %H:%M:%S"
    correct_date_format = "%d/%m/%Y %H:%M:%S" 
    
    try:
        return datetime.datetime.strptime(date_string, incorrect_date_format)
    except ValueError:
        try:
            return datetime.datetime.strptime(date_string, correct_date_format)
        except ValueError:
            return None 