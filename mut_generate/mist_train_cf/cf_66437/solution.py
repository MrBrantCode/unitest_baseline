"""
QUESTION:
Write a function named `convert_time` that takes a list of time strings in the format "HH:MM" (24-hour time) and converts each time to its corresponding 12-hour time format (HH:MM AM/PM). The function should handle edge cases where the hours or minutes are greater than standard measurements (e.g., 25:90 should be converted to 02:30 AM). The function should return the converted times.
"""

from datetime import datetime, timedelta

def convert_time(time_list):
    converted_times = []
    for time in time_list:
        h, m = map(int, time.split(':'))
        total_minutes = h * 60 + m
        d = datetime(1,1,1) + timedelta(minutes=total_minutes)
        converted_times.append(d.strftime("%I:%M %p"))
    return converted_times