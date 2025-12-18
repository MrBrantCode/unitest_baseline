"""
QUESTION:
Write a Python function `is_valid_date_time` that takes a string as input and returns `True` if the string matches the format "DD/MM/YYYY HH:MM:SS AM/PM" and `False` otherwise. The function should enforce the following rules:
- DD is a day of the month from 01 to 31,
- MM is a month from 01 to 12,
- YYYY is a four-digit year from 1800 to 2100,
- HH is an hour from 01 to 12,
- MM is a minute from 00 to 59,
- SS is a second from 00 to 59,
- AM/PM indicates whether the time is before (AM) or after (PM) midday. 
The function should correctly handle edge cases like February 29 on leap years.
"""

from datetime import datetime

def is_valid_date_time(date_string):
    try:
        # Check general date time format with strptime
        datetime.strptime(date_string, '%d/%m/%Y %I:%M:%S %p')
        
        # Additional checking for year range
        year = int(date_string[6:10])
        if year < 1800 or year > 2100:
            return False
    except ValueError:
        return False
    return True