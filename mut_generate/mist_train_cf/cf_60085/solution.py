"""
QUESTION:
Write a function `reformat_date_time` that takes a string in the format 'Day-Month-Year and Hours:Minutes' and returns the string in 'Year-Month-Day and Hours:Minutes' format.
"""

from datetime import datetime

def reformat_date_time(date_string):
    """
    This function takes a string in the format 'Day-Month-Year and Hours:Minutes' 
    and returns the string in 'Year-Month-Day and Hours:Minutes' format.

    Args:
        date_string (str): The input date string.

    Returns:
        str: The reformatted date string.
    """
    # Convert the original string to a datetime object
    date_obj = datetime.strptime(date_string, "%d-%m-%Y %H:%M")

    # Format the datetime object to the desired string
    formatted = date_obj.strftime("%Y-%m-%d %H:%M")

    return formatted