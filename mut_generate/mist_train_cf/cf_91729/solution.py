"""
QUESTION:
Write a function `convert_timestamp(timestamp)` that takes a string `timestamp` in the format "yyyy-mm-dd HH:MM:SS" and returns a string representing the timestamp in the format "Month dd, yyyy HH:MM:SS AM/PM".
"""

from datetime import datetime

def convert_timestamp(timestamp):
    # Convert the timestamp string to a datetime object
    dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
    
    # Format the datetime object as a human readable string
    human_readable_time = dt.strftime("%B %d, %Y %I:%M:%S %p")
    
    return human_readable_time