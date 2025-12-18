"""
QUESTION:
Write a function named `generate_timestamp` that takes a string representing a date and time in the format "MM/DD/YYYY HH:MM:SS" and returns the corresponding timestamp in the format "YYYY-MM-DD HH:MM:SS" in the UTC timezone. The input time is in 24-hour format.
"""

from datetime import datetime
from pytz import timezone

def generate_timestamp(input_str):
    input_format = "%m/%d/%Y %H:%M:%S"
    output_format = "%Y-%m-%d %H:%M:%S"
    
    dt = datetime.strptime(input_str, input_format)
    utc_dt = timezone('UTC').localize(dt)
    output_str = utc_dt.strftime(output_format)
    
    return output_str