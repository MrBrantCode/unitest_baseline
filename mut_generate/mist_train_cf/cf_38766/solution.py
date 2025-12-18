"""
QUESTION:
Write a function `format_date` that takes a date string in the format "YYYY-MM-DD" as input and returns the date in the format "DD del MM del año YYYY".
"""

from datetime import datetime

def format_date(date_str):
    """
    This function formats a given date string from 'YYYY-MM-DD' to 'DD del MM del año YYYY'.

    Args:
        date_str (str): The input date string in the format 'YYYY-MM-DD'.

    Returns:
        str: The formatted date string in the format 'DD del MM del año YYYY'.
    """

    # Convert input date string to datetime object
    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
    
    # Format the date as required and return
    return date_obj.strftime("%d del %m del año %Y")