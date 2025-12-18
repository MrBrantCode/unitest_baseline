"""
QUESTION:
Create a function named `is_valid_date` that takes a string representing a date in the format "dd/mm/yyyy" and returns "Valid date" if the date is valid according to the Gregorian calendar rules and "Invalid date" otherwise. The function should consider the following restrictions:
- The day should be between 1 and 31, depending on the month.
- The month should be between 1 and 12.
- The year should be a positive number.
- The function should account for leap years and the appropriate number of days for each month.
"""

def is_valid_date(date_str):
    try:
        day, month, year = map(int, date_str.split('/'))
        if year < 1:
            return "Invalid date"
        if month < 1 or month > 12:
            return "Invalid date"
        if month in [4, 6, 9, 11] and day > 30:
            return "Invalid date"
        if month == 2:
            if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
                if day > 29:
                    return "Invalid date"
            else:
                if day > 28:
                    return "Invalid date"
        elif day > 31:
            return "Invalid date"
        return "Valid date"
    except ValueError:
        return "Invalid date"