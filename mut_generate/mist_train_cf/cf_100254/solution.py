"""
QUESTION:
Write a function `calculate_time_difference` that calculates the total number of hours between a specific starting time yesterday and a specific ending time today. The function should take the year, month, day, hour, minute, and second of both the start and end times as input, handle non-standard times, and return the total number of hours between them. The input times should be in 24-hour format.
"""

import datetime
from datetime import timedelta

def calculate_time_difference(start_year, start_month, start_day, start_hour, start_minute, start_second, 
                              end_year, end_month, end_day, end_hour, end_minute, end_second):
    # Set the starting time yesterday
    start_time = datetime.datetime(start_year, start_month, start_day, start_hour, start_minute, start_second)
    # Set the ending time today
    end_time = datetime.datetime(end_year, end_month, end_day, end_hour, end_minute, end_second)
    # Calculate the time difference
    time_diff = end_time - start_time
    # Convert the time difference to hours
    total_hours = time_diff.total_seconds() / 3600
    return total_hours