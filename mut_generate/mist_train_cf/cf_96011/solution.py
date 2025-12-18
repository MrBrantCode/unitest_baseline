"""
QUESTION:
Write a function `difference_in_minutes(timestamp1, timestamp2)` that takes two Unix timestamps in seconds as input and returns the difference between them in minutes, rounded down to the nearest whole number. The function should have a time complexity of O(1).
"""

import math

def difference_in_minutes(timestamp1, timestamp2):
    difference = timestamp2 - timestamp1
    return math.floor(difference / 60)