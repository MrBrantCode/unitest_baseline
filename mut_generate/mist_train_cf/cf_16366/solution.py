"""
QUESTION:
Write a function `print_dates(start_date, end_date, output_format='DD/MM/YYYY')` that prints all dates between `start_date` and `end_date` (inclusive) in the specified `output_format`. The function should be able to handle dates in either 'DD/MM/YYYY' or 'MM/DD/YYYY' format, and should automatically swap the dates if `start_date` is after `end_date`. It should also handle leap years correctly and be memory efficient for large date ranges. The function should print an error message and return if the input date format is invalid.
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