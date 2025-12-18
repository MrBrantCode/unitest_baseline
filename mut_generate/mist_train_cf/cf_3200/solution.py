"""
QUESTION:
Write a function named `get_days_in_month` that takes two parameters, `month` and `year`, and returns the number of days in that month for the given year. The function should correctly handle leap years and months with 31, 30, or 28/29 days. The function should also handle invalid months (not between 1 and 12) by returning "Invalid month entered." The function should not handle invalid years (negative, non-integer, or other).
"""

def get_days_in_month(month, year):
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
        return "Invalid month entered."
    
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if is_leap_year(year):
        days_in_month[1] = 29
    
    return days_in_month[month - 1]