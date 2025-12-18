"""
QUESTION:
Write a function `convert_timestamp_and_check_leap_year` that takes a Unix timestamp as input, converts it to a date and time, extracts the year, and checks if it is a leap year. The function should return a message stating whether the year is a leap year or not. The function should handle any potential exceptions.
"""

import datetime

def convert_timestamp_and_check_leap_year(timestamp: int) -> str:
    try:
        date_time = datetime.datetime.fromtimestamp(timestamp)
        year = date_time.year
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return f'The year {year} extracted from the Unix timestamp {timestamp} is a leap year.'
        else:
            return f'The year {year} extracted from the Unix timestamp {timestamp} is not a leap year.'
    except Exception as e:
        return f'An error occurred: {str(e)}'