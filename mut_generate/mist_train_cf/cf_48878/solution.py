"""
QUESTION:
Write a function `days_in_month` that takes two parameters, `Y` and `M`, representing the year and month, respectively, and returns a tuple containing the total number of days in the month and the number of weekdays in the month. The year `Y` is in the range `1583 <= Y <= 2100` and the month `M` is in the range `1 <= M <= 12`.
"""

import calendar

def days_in_month(Y, M):
    _, num_days = calendar.monthrange(Y, M)
    first_day, _ = calendar.monthrange(Y, M)
    weekdays = (num_days - first_day) // 7 * 5 + min(first_day + num_days % 7, 5)
    return num_days, weekdays