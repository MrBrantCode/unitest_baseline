"""
QUESTION:
Write a function `convert_military_to_standard` that takes a string representing a time in military (24-hour) format as input and returns a string representing the equivalent time in standard (12-hour) format. The input string should be in the format HHMM, where HH is the hour (00-23) and MM is the minute (00-59). The output string should be in the format H:MM AM/PM, where H is the hour (1-12) and AM/PM indicates whether the time is in the morning or afternoon/evening.
"""

def convert_military_to_standard(time):
    hours = int(time[:2])
    minutes = time[2:]

    if hours == 0:
        hours = 12
        return f"{hours}:{minutes} AM"
    elif hours > 12:
        hours -= 12
        return f"{hours}:{minutes} PM"
    elif hours == 12:
        return f"{hours}:{minutes} PM"
    else:
        return f"{hours}:{minutes} AM"