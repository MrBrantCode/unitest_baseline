"""
QUESTION:
Write a function `convert_time_to_12_hour(time)` that takes a string of four digits representing time in 24-hour military time format, and returns a string representing the equivalent time in 12-hour civilian time format (e.g., "HH:MM AM/PM"). The input string will be in the format "HHMM" where HH represents hours (00-23) and MM represents minutes (00-59).
"""

def convert_time_to_12_hour(time):
    hrs, mins = int(time[:2]), int(time[2:])
    setting = 'AM' if hrs < 12 else 'PM'
    
    if hrs > 12:
        hrs -= 12

    elif hrs == 0:
        hrs = 12

    return "{:02}:{:02} {}".format(hrs, mins, setting)