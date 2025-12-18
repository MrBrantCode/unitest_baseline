"""
QUESTION:
Create a function named `convert_to_iso_date` that takes a string representing a date as input, converts it into ISO 8601 format, and handles leap years. The function should support various date and time formats, including optional time information. If the input date is invalid, the function should return `None`.
"""

import re
from datetime import datetime

def convert_to_iso_date(date_string):
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
    
    try:
        date_obj = datetime.strptime(date_string, format)
        year = date_obj.year
        is_leap_year = (year % 4 == 0) and (year % 100 != 0 or year % 400 == 0)
    except ValueError:
        return None
    
    if is_leap_year:
        return date_obj.strftime('%Y-%m-%dT%H:%M:%S.%fZ')
    else:
        return date_obj.strftime('%Y-%m-%dT%H:%MZ')