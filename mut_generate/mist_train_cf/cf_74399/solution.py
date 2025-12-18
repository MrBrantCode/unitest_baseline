"""
QUESTION:
Create a function named `count_weekdays` that takes three parameters: `year`, `month`, and `day`. The function should return the total number of a specific weekday (`day`) in a given `month` and `year`. The function should correctly handle leap years and return an error message for invalid inputs. The inputs should be validated to ensure `day` is a valid weekday, `month` is between 1 and 12, and `year` is an integer.
"""

import calendar

def count_weekdays(year, month, day):
    try:
        day_index = list(calendar.day_name).index(day)
    except ValueError:
        return "Invalid Day Entered"

    if not 1 <= month <= 12:
        return "Invalid Month Entered"
    try:
        year = int(year)
    except ValueError:
        return "Invalid Year Entered"
    
    month_calendar = calendar.monthcalendar(year, month)
    total_days = sum(1 for week in month_calendar if week[day_index] != 0)

    return total_days