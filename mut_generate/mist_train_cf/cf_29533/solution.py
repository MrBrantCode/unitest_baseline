"""
QUESTION:
Implement the function `convert_to_12_hour_format` that takes a string representing time in 24-hour format "HH:MM:SS" as input and returns the time in 12-hour format with the appropriate suffix "AM" or "PM". The input time is always valid and in the correct format.
"""

def convert_to_12_hour_format(time_24h):
    hour, minute, second = map(int, time_24h.split(':'))
    
    suffix = "AM"
    if hour >= 12:
        suffix = "PM"
        if hour > 12:
            hour -= 12
    
    if hour == 0:
        hour = 12
    
    return f"{hour}:{minute:02d}:{second:02d} {suffix}"