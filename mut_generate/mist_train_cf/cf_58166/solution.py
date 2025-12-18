"""
QUESTION:
Write a function `has_thirty_days(month, year)` that checks whether a given month in a given year contains exactly 30 days. The function should consider leap years where February has 29 days instead of the usual 28. The month number should be in the range from 1 to 12, and the year should be any integer.
"""

import calendar

def has_thirty_days(month, year):
    days_in_month = calendar.monthrange(year, month)[1]
    return days_in_month == 30