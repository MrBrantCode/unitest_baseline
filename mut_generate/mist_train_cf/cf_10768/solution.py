"""
QUESTION:
Create a function called `get_num_days` that takes two parameters: an integer `month` and an integer `year`, and returns the number of days in the given month. The function should correctly handle leap years.
"""

def get_num_days(month, year):
    # check if the year is a leap year
    if year % 400 == 0 or (year % 100 != 0 and year % 4 == 0):
        leap_year = True
    else:
        leap_year = False
    
    # dictionary to map month number to number of days
    num_days_in_month = {
        1: 31,
        2: 29 if leap_year else 28,
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
    
    # return the number of days for the given month
    return num_days_in_month[month]