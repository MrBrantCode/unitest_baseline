"""
QUESTION:
Write a function named `print_dates` that takes three parameters: `start_date`, `end_date`, and `output_format` (optional, defaults to `"%m/%d/%Y"`). The function should print all dates between `start_date` and `end_date` (inclusive) in the specified `output_format`. 

The function should handle any valid date format for `start_date` and `end_date`, including both 12-hour and 24-hour formats, and should be able to handle dates in either order. It should also handle leap years, edge cases, and dates spanning multiple years or centuries. The function should validate the input dates to ensure they are valid and within a reasonable range. 

If the input dates are invalid, the function should print an error message and return without printing any dates. If the `output_format` is not specified, the function should default to `"%m/%d/%Y"`.
"""

import datetime

def print_dates(start_date, end_date, output_format="%m/%d/%Y"):
    try:
        start_date = datetime.datetime.strptime(start_date, "%m/%d/%Y")
        end_date = datetime.datetime.strptime(end_date, "%m/%d/%Y")
    except ValueError:
        try:
            start_date = datetime.datetime.strptime(start_date, "%d/%m/%Y")
            end_date = datetime.datetime.strptime(end_date, "%d/%m/%Y")
        except ValueError:
            print("Invalid date format. Please use MM/DD/YYYY or DD/MM/YYYY.")
            return
    
    if start_date > end_date:
        start_date, end_date = end_date, start_date
    
    delta = datetime.timedelta(days=1)
    while start_date <= end_date:
        print(start_date.strftime(output_format))
        start_date += delta