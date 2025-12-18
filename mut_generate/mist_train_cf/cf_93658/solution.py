"""
QUESTION:
Implement a function `convert_date(input_date)` that takes a string `input_date` in the format MM/DD/YYYY as input. The function should validate the input date and return it in the format DD-MM-YYYY if valid, otherwise return "Invalid date".
"""

def convert_date(input_date):
    # Split the input_date string into day, month, and year
    date_parts = input_date.split('/')
    
    # Check if the input_date has three parts
    if len(date_parts) != 3:
        return "Invalid date"
    
    # Convert the day, month, and year strings into integers
    day = int(date_parts[1])
    month = int(date_parts[0])
    year = int(date_parts[2])
    
    # Check if the month value is valid (between 1 and 12)
    if month < 1 or month > 12:
        return "Invalid date"
    
    # Check if the day value is valid for the given month and year
    if day < 1 or day > 31:
        return "Invalid date"
    
    # Check for months with 30 days
    if month in [4, 6, 9, 11] and day > 30:
        return "Invalid date"
    
    # Check for February
    if month == 2:
        # Check if it is a leap year
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            if day > 29:
                return "Invalid date"
        else:
            if day > 28:
                return "Invalid date"
    
    # Convert the date to the required format (DD-MM-YYYY)
    converted_date = str(day).zfill(2) + '-' + str(month).zfill(2) + '-' + str(year)
    
    return converted_date