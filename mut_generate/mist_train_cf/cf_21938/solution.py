"""
QUESTION:
Create a function `validate_dates(date1, date2)` that takes two date strings in the format "yyyy-mm-dd" as input and returns `True` if the dates are in increasing order, adhere to the Gregorian calendar system, and fall within the range of 2000-01-01 to 2025-12-31. Otherwise, it should return `False`. The function should consider leap years and the correct number of days in each month.
"""

def validate_dates(date1, date2):
    # Check if dates are in "yyyy-mm-dd" format
    if len(date1) != 10 or len(date2) != 10:
        return False

    # Check if dates are within the range 2000-01-01 to 2025-12-31
    if date1 < "2000-01-01" or date1 > "2025-12-31" or date2 < "2000-01-01" or date2 > "2025-12-31":
        return False

    # Check if dates are in increasing order
    if date1 >= date2:
        return False

    # Check if dates adhere to the Gregorian calendar system
    year1, month1, day1 = map(int, date1.split('-'))
    year2, month2, day2 = map(int, date2.split('-'))

    # Check leap year for date1
    if year1 % 4 == 0 and (year1 % 100 != 0 or year1 % 400 == 0):
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if day1 > days_in_month[month1 - 1]:
        return False

    # Check leap year for date2
    if year2 % 4 == 0 and (year2 % 100 != 0 or year2 % 400 == 0):
        days_in_month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    else:
        days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    if day2 > days_in_month[month2 - 1]:
        return False

    return True