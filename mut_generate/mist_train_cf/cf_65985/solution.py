"""
QUESTION:
Write a function `convert_timestamp` that takes a string timestamp in the format 'Year-Month-Day Hours:Minutes' and returns the timestamp in the format 'Day-Month-Year Hours:Minutes'. The input timestamp is a string, and the output should also be a string.
"""

from datetime import datetime

def convert_timestamp(timestamp):
    """
    This function takes a string timestamp in the format 'Year-Month-Day Hours:Minutes' 
    and returns the timestamp in the format 'Day-Month-Year Hours:Minutes'.

    Args:
    timestamp (str): The input timestamp string.

    Returns:
    str: The timestamp in the desired format.
    """
    # convert the string to a datetime object, specifying its current format
    dt = datetime.strptime(timestamp, '%Y-%m-%d %H:%M')
    # convert the datetime object back to a string, but in the desired format
    desired_timestamp = dt.strftime('%d-%m-%Y %H:%M')
    return desired_timestamp