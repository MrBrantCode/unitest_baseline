"""
QUESTION:
Write a function `compare_dates(date1, date2)` that takes two date objects as input and returns a string indicating whether `date1` is before, after, or the same as `date2`. The function should return "Before" if `date1` is before `date2`, "After" if `date1` is after `date2`, and "Same" if `date1` is the same as `date2`.
"""

from datetime import date

def compare_dates(date1, date2):
    if date1 < date2:
        return "Before"
    elif date1 > date2:
        return "After"
    else:
        return "Same"