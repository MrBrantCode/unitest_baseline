"""
QUESTION:
Write a function named `format_date_to_iso` that takes a string representing a date in the format 'Month Day(th/nd/rd), Year' (e.g., 'January 5th, 2021') and returns a string representing the date in ISO 8601 format (YYYY-MM-DD).
"""

import re
from datetime import datetime

def format_date_to_iso(date_str):
    """
    Convert a date string from 'Month Day(th/nd/rd), Year' to ISO 8601 format (YYYY-MM-DD).
    
    Args:
        date_str (str): The date string to convert.

    Returns:
        str: The date in ISO 8601 format.
    """
    # Use regular expression to remove the day's suffix (th, nd, rd) from the date string
    date_str = re.sub(r'(\d)(st|nd|rd|th)', r'\1', date_str)
    
    # Parse the date string into a datetime object
    date_obj = datetime.strptime(date_str, '%B %d, %Y')
    
    # Format the datetime object into ISO 8601 format
    iso_date_str = date_obj.strftime('%Y-%m-%d')
    
    return iso_date_str