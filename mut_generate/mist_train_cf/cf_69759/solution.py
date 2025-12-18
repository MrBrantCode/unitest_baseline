"""
QUESTION:
Write a function `date_to_unix` that takes a date string in the format YYYY-MM-DD and returns its corresponding UNIX timestamp. The function should correctly handle leap years and raise an error if the input date string is invalid.
"""

import datetime 
import time 

def date_to_unix(date_str):
    # Parsing the date string format to datetime object
    try:
        date = datetime.datetime.strptime(date_str, '%Y-%m-%d')
    except Exception as e:
        return f"Error: {e}. Please input a valid date in the 'YYYY-MM-DD' format."
    # Convert the datetime object to UNIX timestamp
    unix_timestamp = time.mktime(date.timetuple())
    
    return unix_timestamp