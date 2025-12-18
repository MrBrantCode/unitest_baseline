"""
QUESTION:
Write a Python function named `validate_date` that takes a string in the format 'YYYY/MM/DD' as input. The function should return True if the date is valid in the Gregorian calendar and False otherwise. The function should handle leap years correctly and consider dates before 1583 as invalid.
"""

from datetime import datetime

def validate_date(date_str):
    try:
        date_obj = datetime.strptime(date_str, '%Y/%m/%d')
        if date_obj.year < 1583:
            return False
        datetime(date_obj.year, date_obj.month, date_obj.day)
        return True
    except ValueError:
        return False