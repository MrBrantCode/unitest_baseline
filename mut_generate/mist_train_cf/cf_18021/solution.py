"""
QUESTION:
Write a function `number_of_days(month, year)` that takes two integers as input, `month` and `year`, and returns the number of days in that month, considering leap years. The function should return an error message if the month or year is invalid (i.e., month < 1 or month > 12, year < 0).
"""

def number_of_days(month, year):
    def is_leap_year(year):
        if year % 4 == 0:
            if year % 100 == 0:
                if year % 400 == 0:
                    return True
                else:
                    return False
            else:
                return True
        else:
            return False

    if month < 1 or month > 12:
        return "Invalid month"

    if year < 0:
        return "Invalid year"

    days_in_month = {
        1: 31,
        2: 28,
        3: 31,
        4: 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31
    }

    if is_leap_year(year) and month == 2:
        return 29
    else:
        return days_in_month[month]