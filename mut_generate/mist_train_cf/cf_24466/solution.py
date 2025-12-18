"""
QUESTION:
Write a function named `convert_epoch_to_human_readable` that takes an integer representing epoch time in seconds as input and returns a string representing the corresponding date and time in human-readable format (YYYY-MM-DD, HH:MM:SS AM/PM UTC).
"""

from datetime import datetime

def convert_epoch_to_human_readable(epoch_time):
    """
    Converts epoch time in seconds to human-readable format (YYYY-MM-DD, HH:MM:SS AM/PM UTC).

    Args:
    epoch_time (int): Time in seconds since January 1, 1970.

    Returns:
    str: Human-readable date and time string.
    """
    # Convert epoch time to datetime object
    date_time = datetime.utcfromtimestamp(epoch_time)
    
    # Format datetime object into human-readable string
    human_readable_time = date_time.strftime('%Y-%m-%d, %I:%M:%S %p UTC')
    
    return human_readable_time