"""
QUESTION:
Write a function called `difference_in_minutes` that takes two Unix timestamps as input and returns the absolute difference between them in minutes, rounded down to the nearest whole number.
"""

import math

def difference_in_minutes(timestamp1, timestamp2):
    larger_timestamp = max(timestamp1, timestamp2)
    smaller_timestamp = min(timestamp1, timestamp2)
    difference = larger_timestamp - smaller_timestamp
    difference_in_minutes = math.floor(difference / 60)
    return difference_in_minutes