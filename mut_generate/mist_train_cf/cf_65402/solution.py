"""
QUESTION:
Design a function named `get_weekday_count` that takes in a year, a month, and a list of weekday names as parameters. The function should return a dictionary where the keys are the weekday names provided in the input list and the values are the number of occurrences of each weekday in the given month.

The function should use the standard Python library for date and time-related functionality. The input weekday names should be matched to their corresponding integer values, where "Monday" maps to 0 and "Sunday" maps to 6. The function should only count the weekdays that are present in the input list.
"""

def get_weekday_count(year, month, day_names):
    import calendar
    import datetime
    weekday_map = {"Monday": 0, "Tuesday": 1, "Wednesday": 2, "Thursday": 3, "Friday": 4, "Saturday": 5, "Sunday": 6}
    weekday_count = {weekday: 0 for weekday in day_names}

    for i in range(1, calendar.monthrange(year, month)[1] + 1):
        day = datetime.datetime(year, month, i)
        if calendar.day_name[day.weekday()] in weekday_count:
            weekday_count[calendar.day_name[day.weekday()]] += 1
    return weekday_count