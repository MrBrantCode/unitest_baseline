"""
QUESTION:
Write a function named `is_valid_date` that checks if a given string `date_str` in the format "MM/DD/YYYY" represents a valid date, including leap years. The function should return a boolean value indicating whether the date is valid.
"""

def is_valid_date(date_str):
    # Check if the string has the correct length
    if len(date_str) != 10:
        return False

    # Split the string into month, day, and year
    month, day, year = date_str.split('/')

    # Check if the month is a valid number
    try:
        month = int(month)
        if month < 1 or month > 12:
            return False
    except ValueError:
        return False

    # Check if the day is a valid number
    try:
        day = int(day)
        if day < 1 or day > 31:
            return False
    except ValueError:
        return False

    # Check if the year is a valid number
    try:
        year = int(year)
    except ValueError:
        return False

    # Check if it's a leap year
    if month == 2 and day == 29:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            return True
        else:
            return False

    # Check if the day is valid for the given month
    if month == 2 and day > 28:
        return False
    elif month in [4, 6, 9, 11] and day > 30:
        return False

    return True