"""
QUESTION:
Write a function named `convert_date_to_timestamp` that takes a date string and its format as input and returns the equivalent timestamp. The function should be able to handle any date format. The input date string and its format will be provided as a string, and the output should be in seconds since the epoch (January 1, 1970).
"""

import time
from datetime import datetime

def convert_date_to_timestamp(date_str, format="%d/%m/%Y"):
    dt = datetime.strptime(date_str, format)
    return time.mktime(dt.timetuple())