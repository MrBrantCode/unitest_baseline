"""
QUESTION:
Convert a given date string to ISO 8601 format using the function `convert_to_iso_date`. The function should handle various date and time formats, including optional time information, and properly identify and handle leap years. If the date string is invalid, the function should return `None`.
"""

import re
from datetime import datetime

def convert_to_iso_date(date_string):
    # Determine the format of the input date string
    format = None
    if re.match('^\d{4}-\d{2}-\d{2}$', date_string):
        format = '%Y-%m-%d'
    elif re.match('^\d{1,2}\/\d{1,2}\/\d{4}$', date_string):
        format = '%m/%d/%Y'
    elif re.match('^\d{4}\/\d{1,2}\/\d{1,2}$', date_string):
        format = '%Y/%m/%d'
    elif re.match('^\d{1,2}\-\d{1,2}\-\d{4}$', date_string):
        format = '%m-%d-%Y'
    elif re.match('^\d{4}\-\d{1,2}\-\d{1,2}$', date_string):
        format = '%Y-%m-%d'
    elif re.match('^\d{1,2}\/\d{1,2}\/\d{4} \d{1,2}:\d{2}:\d{2}$', date_string):
        format = '%m/%d/%Y %H:%M:%S'
    elif re.match('^\d{4}\/\d{1,2}\/\d{1,2} \d{1,2}:\d{2}:\d{2}$', date_string):
        format = '%Y/%m/%d %H:%M:%S'
    elif re.match('^\d{1,2}\-\d{1,2}\-\d{4} \d{1,2}:\d{2}:\d{2}$', date_string):
        format = '%m-%d-%Y %H:%M:%S'
    elif re.match('^\d{4}\-\d{1,2}\-\d{1,2} \d{1,2}:\d{2}:\d{2}$', date_string):
        format = '%Y-%m-%d %H:%M:%S'
    else:
        return None
    
    # Parse the date string and check if it is a leap year
    try:
        date_obj = datetime.strptime(date_string, format)
        year = date_obj.year
        is_leap_year = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
    except ValueError:
        return None
    
    # Format the date as ISO 8601
    if is_leap_year:
        return date_obj.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    else:
        return date_obj.strftime('%Y-%m-%dT%H:%MZ')