"""
QUESTION:
Create a function `count_weekdays(year, month, day=None)` to calculate the total number of weekdays in a specific month and year. The function should return a dictionary containing the count of each weekday (e.g., Monday, Tuesday) in the month. If the `day` parameter is provided, the function should return a dictionary with the count of the specified weekday. The function should use the Gregorian calendar, as Python's standard library does not directly support the Julian calendar.
"""

import calendar

def count_weekdays(year, month, day=None):
    # get the weekday and the total days in the month
    first_day, num_days = calendar.monthrange(year, month)
    # create a list representing the weekdays of each day in the month [0,1,2,....]
    days = [(first_day+i)%7 for i in range(num_days)]
    
    if day is None:  # if no specific day is given
        # return the count of each weekday
        return {calendar.day_name[i]: days.count(i) for i in range(7)}
    else:
        # return the count of the specific weekday
        return {calendar.day_name[day]: days.count(day)}