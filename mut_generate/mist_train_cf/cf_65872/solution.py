"""
QUESTION:
Write a function `days_between(d1, d2)` that calculates the absolute difference in days between two dates `d1` and `d2` in the format "YYYY-MM-DD".
"""

import datetime

def days_between(d1, d2):
    d1 = datetime.datetime.strptime(d1, "%Y-%m-%d")
    d2 = datetime.datetime.strptime(d2, "%Y-%m-%d")
    return abs((d2 - d1).days)