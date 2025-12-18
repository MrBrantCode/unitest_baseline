"""
QUESTION:
Implement a function `convert_date(input_date)` that takes a string `input_date` in the format MM/DD/YYYY, validates the input date, converts it into the format DD-MM-YYYY, and checks if it falls on a weekday. The function should return a tuple containing the converted date as a string and a boolean value indicating whether it falls on a weekday. If the input date is invalid, the function should return "Invalid date" for the converted date and False for the weekday.
"""

import calendar

def convert_date(input_date):
    # Split the input_date string into month, day, and year
    month, day, year = input_date.split('/')
    
    # Validate the month, day, and year
    if not (1 <= int(month) <= 12):
        return "Invalid date", False
    if not (1 <= int(day) <= 31):
        return "Invalid date", False
    if not (1000 <= int(year) <= 9999):
        return "Invalid date", False
    
    # Convert the date into the format DD-MM-YYYY
    converted_date = f"{day}-{month}-{year}"
    
    # Check if the converted date falls on a weekday
    weekday = calendar.weekday(int(year), int(month), int(day))
    is_weekday = weekday < 5
    
    return converted_date, is_weekday