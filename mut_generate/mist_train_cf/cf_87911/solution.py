"""
QUESTION:
Write a function `is_valid_date` that checks if a given string represents a valid date in the format "MM/DD/YYYY". The input string must be exactly 10 characters long and contain a date where the year is between 1900 and 2100 (inclusive), the month is between 01 and 12 (inclusive), and the day is between 01 and 31 (inclusive). The function must also account for leap years and the varying number of days in each month.
"""

def is_valid_date(date_string):
    # Check if the string has the correct length
    if len(date_string) != 10:
        return False

    # Split the string into month, day, and year
    month = int(date_string[0:2])
    day = int(date_string[3:5])
    year = int(date_string[6:10])

    # Check if the year is within the valid range
    if year < 1900 or year > 2100:
        return False

    # Check if the month is within the valid range
    if month < 1 or month > 12:
        return False

    # Check if the day is within the valid range
    if day < 1 or day > 31:
        return False

    # Check if the day is valid for the given month and year
    if month == 2:
        if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
            if day > 29:
                return False
        else:
            if day > 28:
                return False
    elif month in [4, 6, 9, 11]:
        if day > 30:
            return False

    return True