"""
QUESTION:
Write a function `convert_to_24hr` that takes a string representing time in 12-hour format (HH:MM:SS.SSSAM/PM) as input, where HH is hours, MM is minutes, SS is seconds, and SSS is milliseconds. The function should return the equivalent time in 24-hour format (HH:MM:SS.SSS). The function should handle cases where the input time is 12 AM or 12 PM correctly.
"""

from datetime import datetime

def convert_to_24hr(time_str):
    # Separate the time elements and the period
    period = time_str[-2:]

    # Extract the hours, minutes, seconds and milliseconds
    time_parts = time_str[:-2].split(":")
    
    hours = int(time_parts[0])
    minutes = int(time_parts[1])
    seconds = int(time_parts[2].split('.')[0])
    milliseconds = int(time_parts[2].split('.')[1])

    # Handling special case where time is 12 AM
    if period == "AM" and hours == 12:
        hours = 0
    
    # Otherwise, if it isn't AM, add 12 hours (so long it isn't the 12th hour)
    elif period == "PM" and hours != 12:
        hours += 12

    # Formatting it to a readable 24 hour format
    result = "{:02}:{:02}:{:02}.{}".format(hours, minutes, seconds, milliseconds)

    return result