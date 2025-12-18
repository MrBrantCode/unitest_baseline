"""
QUESTION:
Create a function `check_date` that takes a string as input and returns the date in 'YYYY-MM-DD' format if the string represents a valid date between the years 1000 and 9999. The function should handle multiple date formats, including 'Jan 31, 1999', '31 Jan, 1999', '1999/01/31', etc. If the input string is not a valid date, return 'Invalid date'.
"""

from datetime import datetime

def check_date(string):
    # List of date formats
    formats = ['%Y-%m-%d', '%d-%m-%Y', '%m-%d-%Y', '%B %d, %Y', 
               '%d %B, %Y', '%Y/%m/%d', '%d/%m/%Y', '%m/%d/%Y',
               '%b %d, %Y', '%d %b, %Y']

    for date_format in formats:
        try:
            # If the string is a valid date according to the current format
            date = datetime.strptime(string, date_format)

            # If the year is in the range 1000-9999
            if 1000 <= date.year <= 9999:
                return date.strftime('%Y-%m-%d')

        except ValueError:
            pass

    return 'Invalid date'