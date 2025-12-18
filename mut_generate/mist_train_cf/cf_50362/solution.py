"""
QUESTION:
Create a function named `find_weekday` that takes a date string in 'DDMMYYYY' format as input and returns the corresponding weekday according to the Gregorian calendar system. The function should handle invalid input, including non-string inputs, invalid date formats, and non-existent dates, and return an error message in such cases.
"""

from datetime import datetime

def find_weekday(date):
    try:
        if not isinstance(date, str):
            return "Error: Input should be a string."
        if len(date) != 8:
            return "Error: Date should be in 'DDMMYYYY' format."
        
        day = int(date[:2])
        month = int(date[2:4])
        year = int(date[4:])
        
        input_date = datetime(year, month, day)
        
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        return weekdays[input_date.weekday()]
        
    except ValueError:
        return "Error: Invalid date."