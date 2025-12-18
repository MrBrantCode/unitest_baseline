"""
QUESTION:
Create a function `convert_timestamp(timestamp)` that takes a string representing a timestamp in the format "yyyy-MM-dd HH:mm:ss" and returns the equivalent timestamp in ISO 8601 format with the time zone offset. The function should handle invalid timestamp formats by returning an error message. The time complexity should not exceed O(n), where n is the length of the input timestamp, and the space complexity should not exceed O(1).
"""

from datetime import datetime

def convert_timestamp(timestamp):
    try:
        dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        iso8601_string = dt.isoformat()
        return iso8601_string
    except ValueError:
        return "Invalid timestamp format"