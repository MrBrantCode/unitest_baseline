"""
QUESTION:
Convert a given timestamp in the format "yyyy-MM-dd HH:mm:ss" to ISO 8601 format with the time zone offset using the function `convert_timestamp(timestamp)`. Ensure the solution handles errors that may occur during the conversion process and provides an error message for invalid timestamp formats. The solution should have a time complexity of O(n), where n is the length of the input timestamp, and a space complexity of O(1).
"""

from datetime import datetime

def convert_timestamp(timestamp):
    try:
        # Parse the input timestamp string using datetime.strptime()
        dt = datetime.strptime(timestamp, "%Y-%m-%d %H:%M:%S")
        
        # Get the ISO 8601 formatted string with the time zone offset using datetime.isoformat()
        iso8601_string = dt.isoformat()
        
        # Return the ISO 8601 formatted string with the time zone offset
        return iso8601_string
        
    except ValueError:
        # Handle the case where the input timestamp is not in the correct format
        return "Invalid timestamp format"