"""
QUESTION:
Create a function named `convert_time` that takes a string representing time as input and returns the time in the opposite format. If the input time is in 12-hour format (with AM/PM), convert it to 24-hour (military) format, and if the input time is in 24-hour format, convert it to 12-hour format with AM/PM. The function should handle midnight and noon correctly and include error handling for invalid input formats, returning an error message for times not in the 'HH:MM AM/PM' or 'HH:MM' format.
"""

from datetime import datetime

def convert_time(time):
    # Error handling for invalid format
    try:
        if 'AM' in time or 'PM' in time:
            # Convert 12-hour format to 24-hour (military) format
            military_time = datetime.strptime(time, "%I:%M %p")
            return military_time.strftime("%H:%M")
        else:
            # Convert 24-hour (military) format to 12-hour format
            standard_time = datetime.strptime(time, "%H:%M")
            return standard_time.strftime("%I:%M %p")
    except ValueError:
        return "Invalid time format. Please input time as 'HH:MM AM/PM' or 'HH:MM'"