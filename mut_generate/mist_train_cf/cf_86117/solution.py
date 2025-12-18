"""
QUESTION:
Write a function named `validate_dates` that takes a list of date strings as input. The input dates should be in the format 'YYYY-MM-DD' and in increasing chronological order. If the input dates are valid and in order, the function should return `True`; otherwise, it should return `False` and print an error message. The function should handle cases where the input dates are not in the correct format or are not in increasing order.
"""

from datetime import datetime

def validate_dates(date_list):
    # Check if all are valid dates
    try:
        # Convert each date string to datetime object
        parsed_dates = [datetime.strptime(date, '%Y-%m-%d') for date in date_list]
    except ValueError:
        print("One or more of the input dates are not valid.")
        return False
        
    # Check if list is in ascending order
    for i in range(len(parsed_dates) - 1):
        if parsed_dates[i] > parsed_dates[i + 1]:
            print("Dates are not in ascending order.")
            return False

    return True