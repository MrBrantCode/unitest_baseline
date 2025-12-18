"""
QUESTION:
Write a function `print_dates(start_date, end_date, output_format='DD/MM/YYYY')` that prints out all dates between two given dates in Python. 

- The function should accept the start_date and end_date as strings in any valid date format and handle leap years correctly. 
- The function should be able to handle edge cases such as when the start_date and end_date are the same, or when the date range spans multiple years.
- The function should be memory efficient and not use excessive memory, even for large date ranges.
- The function should provide an option to output the dates in a specific format.
"""

from datetime import datetime, timedelta

def print_dates(start_date, end_date, output_format='DD/MM/YYYY'):
    formats = {
        'DD/MM/YYYY': '%d/%m/%Y',
        'MM/DD/YYYY': '%m/%d/%Y',
        # Add more formats if needed
    }
    
    try:
        start = datetime.strptime(start_date, '%d/%m/%Y')
        end = datetime.strptime(end_date, '%d/%m/%Y')
    except ValueError:
        try:
            start = datetime.strptime(start_date, '%m/%d/%Y')
            end = datetime.strptime(end_date, '%m/%d/%Y')
        except ValueError:
            print('Invalid date format. Please use DD/MM/YYYY or MM/DD/YYYY')
            return
    
    if start > end:
        start, end = end, start
    
    delta = timedelta(days=1)
    while start <= end:
        print(start.strftime(formats[output_format]))
        start += delta