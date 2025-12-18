"""
QUESTION:
Implement a function `calculate_interval` that takes two date strings in the format "mm/dd/yyyy" as input and returns the difference between the two dates in days. The function should be able to handle dates in the past and future. The input dates are in the format "mm/dd/yyyy" and the output should be the absolute difference in days.
"""

from datetime import datetime

def calculate_interval(date1, date2):
    # format the date strings into datetime objects
    date_format = "%m/%d/%Y"
    a = datetime.strptime(date1, date_format)
    b = datetime.strptime(date2, date_format)
    
    # calculate the difference between the two dates
    delta = b - a

    return abs(delta.days)