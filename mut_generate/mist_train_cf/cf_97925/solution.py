"""
QUESTION:
Write a function `calculate_time_difference` that takes two `datetime` objects as input, representing a specific time yesterday and a specific time today, and returns the total number of hours between them. The input times are in the format `year, month, day, hour, minute, second`. The function should be able to handle specific times with seconds and calculate the time difference accurately.
"""

import datetime

def calculate_time_difference(start_time, end_time):
    time_diff = end_time - start_time
    total_hours = time_diff.total_seconds() / 3600
    return total_hours