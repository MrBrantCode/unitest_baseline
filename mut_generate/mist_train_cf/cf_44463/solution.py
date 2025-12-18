"""
QUESTION:
Write a function to format a date in the format 'MM-dd-yy'. The input date is in a format that can be parsed into a Date object. Replace the 'date' part in the given template with the formatted date.
"""

from datetime import datetime

def format_date(entity_name):
    """
    Formats a date in 'MM-dd-yy' format.

    Args:
        entity_name (str): The date in a format that can be parsed into a Date object.

    Returns:
        str: The formatted date in 'MM-dd-yy' format.
    """
    date = datetime.strptime(entity_name, '%Y-%m-%d') # Assuming input date is in 'YYYY-MM-DD' format
    return date.strftime('%m-%d-%y')