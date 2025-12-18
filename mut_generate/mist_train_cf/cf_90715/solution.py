"""
QUESTION:
Implement a function `convert_date_format(date_string)` that takes a string `date_string` in the format "MM/DD/YYYY" and returns the date in the format "DD-MM-YYYY", correctly handling leap years. The function should be able to parse the input date string, validate it, and return the converted date string.
"""

from datetime import datetime

def convert_date_format(date_string):
    # Parse the input date string in the format MM/DD/YYYY
    date = datetime.strptime(date_string, "%m/%d/%Y")
    
    # Convert the date to the desired format DD-MM-YYYY
    converted_date = date.strftime("%d-%m-%Y")
    
    return converted_date