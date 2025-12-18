"""
QUESTION:
Write a function `print_dates` that takes two string parameters `start_date` and `end_date` representing dates in either MM/DD/YYYY or DD/MM/YYYY format, and an optional string parameter `output_format` specifying the output date format. The function should print all dates between `start_date` and `end_date` (inclusive) in the specified output format, handling any order of input dates, leap years, edge cases, and date ranges spanning multiple years or centuries. If the input date format is invalid, the function should print an error message and return.
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