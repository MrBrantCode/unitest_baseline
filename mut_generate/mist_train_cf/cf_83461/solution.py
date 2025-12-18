"""
QUESTION:
Write a function `convert24to12(time24)` that takes a string representing time in 24-hour format (HH:MM) and returns the equivalent time in 12-hour format (HH:MM AM/PM). The input time string will always be in the format HH:MM, and the output should use "AM" for times before 12:00 PM and "PM" for times at or after 12:00 PM.
"""

def convert24to12(time24):
    time24 = time24.split(":")
    hours = int(time24[0])
    minutes = time24[1]
    
    if hours == 0:
        return f"12:{minutes} AM"
    elif hours == 12:
        return f"12:{minutes} PM"
    elif hours > 12:
        return f"{hours - 12}:{minutes} PM"
    else:
        return f"{hours}:{minutes} AM"