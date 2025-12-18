"""
QUESTION:
Write a function `process_satellite_time` that takes a string in the format `:(year), (month), (day), (hour), (minute), (second)` as input, extracts the time components, and returns them as a dictionary with keys "year", "month", "day", "hour", "minute", and "second". The input string will always be in the correct format.
"""

import re

def process_satellite_time(input_string):
    time_pattern = r':\((\d+), (\d+), (\d+), (\d+), (\d+), (\d+\.\d+)\)'
    satellite_time = re.search(time_pattern, input_string)
    year = int(satellite_time.group(1))
    month = int(satellite_time.group(2))
    day = int(satellite_time.group(3))
    hour = int(satellite_time.group(4))
    minute = int(satellite_time.group(5))
    second = float(satellite_time.group(6))
    
    time_components = {
        "year": year,
        "month": month,
        "day": day,
        "hour": hour,
        "minute": minute,
        "second": second
    }
    return time_components