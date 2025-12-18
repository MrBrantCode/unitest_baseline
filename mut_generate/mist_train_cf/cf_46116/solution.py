"""
QUESTION:
Create a function `hex_to_standard_time` that takes a hexadecimal string representing a Unix timestamp as input and returns the corresponding standard date/time format. The hexadecimal string should be converted to decimal (base 16 to base 10) and then to a date/time format that is understandable for an average user. The input hexadecimal string represents the number of seconds since the Unix epoch time (January 1, 1970, 00:00:00).
"""

import datetime

def hex_to_standard_time(hex_timestamp):
    """
    Converts a hexadecimal string representing a Unix timestamp to a standard date/time format.
    
    Parameters:
    hex_timestamp (str): A hexadecimal string representing a Unix timestamp.
    
    Returns:
    str: The corresponding standard date/time format.
    """
    dec_timestamp = int(hex_timestamp, 16)
    standard_timestamp = datetime.datetime.fromtimestamp(dec_timestamp)
    return standard_timestamp