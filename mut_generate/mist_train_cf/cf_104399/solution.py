"""
QUESTION:
Write a function named `convert_timestamp` that takes a string timestamp in the format "yyyy-mm-dd HH:MM:SS" as input, and returns the corresponding human readable time in the format "Month dd, yyyy HH:MM:SS AM/PM". The input timestamp string will always be valid and within the range of years from 1970 to 2100.
"""

from datetime import datetime

def convert_timestamp(timestamp):
    # Convert the string timestamp to a datetime object
    dt_object = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    
    # Convert the datetime object to the desired format
    formatted_time = dt_object.strftime("%B %d, %Y %I:%M:%S %p")
    
    return formatted_time