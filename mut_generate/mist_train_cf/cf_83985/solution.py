"""
QUESTION:
Write a function `time_to_minutes(time_str)` that takes a string `time_str` representing the time in 12-hour format (e.g., "12:30PM") and returns the equivalent time in minutes. The input string will always be in the format "HH:MMAM" or "HH:MMPM", where HH represents the hour and MM represents the minutes. The function should handle both AM and PM cases correctly.
"""

def time_to_minutes(time_str):
    hour, minute_with_ampm = time_str[:-2].split(":")
    hour, minute = int(hour), int(minute_with_ampm)
    ampm = time_str[-2:]
    
    if hour == 12:
        hour = 0
    if ampm == "PM":
        hour += 12
    
    minutes = hour * 60 + minute
    return minutes