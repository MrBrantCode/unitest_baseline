"""
QUESTION:
Create a function called `validate_date` that takes a date string in the 'dd/mm/yyyy' format and returns True if the date is valid and in the correct format, or an error message if it's not. The function should be able to handle leap years correctly.
"""

from datetime import datetime

def entrance(date):
    try:
        # Check for correct date format
        # If the format is incorrect, it raises a ValueError exception
        dt = datetime.strptime(date, '%d/%m/%Y')

        # If the date is valid, return True
        return True
    except ValueError:
        # If the date is not valid, return error message
        return 'Invalid date or date format. It should be dd/mm/yyyy.'