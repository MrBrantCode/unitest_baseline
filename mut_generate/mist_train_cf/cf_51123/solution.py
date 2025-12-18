"""
QUESTION:
Write a function named `convert_time` that takes three parameters: `input_time`, `input_zone`, and `output_zone`. The function should convert `input_time` from `input_zone` to `output_zone`. The `input_time` should be a string in 24-hour format (HH:MM). The `input_zone` and `output_zone` should be strings representing valid time zones in the format accepted by the pytz library (e.g., "Asia/Kolkata", "America/Los_Angeles"). The function should return the converted time as a string in 24-hour format (HH:MM). If the input time or zones are incorrect or not supported, the function should return an error message. The function should also handle Daylight Saving Time changes.
"""

from datetime import datetime
from pytz import timezone

def convert_time(input_time, input_zone, output_zone):
    try:
        # Try to get the timezone objects
        input_tz = timezone(input_zone)
        output_tz = timezone(output_zone)
    except:
        return "Invalid timezone"

    # Convert the input string time to a datetime object
    try:
       dt = datetime.strptime(input_time, "%H:%M").replace(tzinfo=input_tz)
    except:
        return "Invalid time format. Please use 24-hour format (e.g., 23:59)"

    # Convert to the output timezone
    converted_time = dt.astimezone(output_tz)
    
    return converted_time.strftime("%H:%M")