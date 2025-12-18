"""
QUESTION:
Develop a function `time_diff` that takes three inputs: two time strings `time1` and `time2` in 24-hour format "HH:MM:SS", and a timezone difference `timezone_diff` in hours. The function should return a string representing the absolute difference between `time1` and `time2` in hours, minutes, and seconds, adjusted for the given timezone difference.
"""

from datetime import datetime

def time_diff(time1, time2, timezone_diff):
    FMT = '%H:%M:%S'
    tdelta = datetime.strptime(time2, FMT) - datetime.strptime(time1, FMT)
    
    # If difference is negative, make it positive
    if tdelta.days < 0:
        tdelta = datetime.strptime(time1, FMT) - datetime.strptime(time2, FMT)
        
    hours = tdelta.seconds // 3600
    minutes = (tdelta.seconds // 60) % 60
    seconds = tdelta.seconds % 60
    
    # Add the timezone difference to the hours
    hours += timezone_diff

    return '{} hour(s) {} minute(s) {} second(s)'.format(hours, minutes, seconds)