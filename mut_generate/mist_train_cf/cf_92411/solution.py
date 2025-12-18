"""
QUESTION:
Write a function `compare_dates` that compares two date objects and returns a string indicating whether the first date is "Before", "After", or "Same" as the second date. The function should take two date objects as input.
"""

from datetime import date

def compare_dates(date1, date2):
    if date1 < date2:
        return "Before"
    elif date1 > date2:
        return "After"
    else:
        return "Same"