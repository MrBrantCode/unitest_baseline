"""
QUESTION:
Create a Python function `reformat_date(error_date, error_format)` to reformat a given date string `error_date` into a specified date format `error_format`. The `error_date` should be in the format "YYYY-MM-DD" and `error_format` should be a valid Python strftime format string. If `error_date` or `error_format` is not a string, or if the date parsing fails, the function should return an error message.
"""

import datetime

def reformat_date(error_date, error_format):
    if not isinstance(error_date, str):
        return "Invalid date. Please, provide a string date in the correct format"
    
    if not isinstance(error_format, str):
        return "Invalid format. Please, provide a string format in the correct format"
    
    try:
        date_object = datetime.datetime.strptime(error_date, "%Y-%m-%d")
        return date_object.strftime(error_format)
    
    except ValueError as e:  
        return "Failed to reformat date due to: " + str(e)