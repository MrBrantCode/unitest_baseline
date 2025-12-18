"""
QUESTION:
Create a function named `is_valid_date` that takes a string representing a date in the format "MM/DD/YYYY" and returns a boolean indicating whether the date is valid. The function should consider leap years and months with different numbers of days. The input string is expected to be in the specified format, but the function should handle invalid inputs.
"""

def is_valid_date(date):
    try:
        month, day, year = map(int, date.split('/'))
        if month < 1 or month > 12:
            return False
        if day < 1 or day > 31:
            return False
        if year < 1000 or year > 9999:
            return False
        if month == 2:
            if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):
                if day > 29:
                    return False
            elif day > 28:
                return False
        elif month in [4, 6, 9, 11]:
            if day > 30:
                return False
        return True
    except ValueError:
        return False