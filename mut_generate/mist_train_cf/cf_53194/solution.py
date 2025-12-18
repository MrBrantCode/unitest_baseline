"""
QUESTION:
Create a function `convert_time` that takes three parameters: `input_tzone` (the input time zone), `output_tzone` (the output time zone), and `input_time` (the input time in the format "YYYY-MM-DD HH:MM"). The function should convert the `input_time` from the `input_tzone` to the `output_tzone`, considering daylight savings time, and return the converted time.
"""

from datetime import datetime
import pytz

def convert_time(input_tzone, output_tzone, input_time):
    # Creating timezone objects
    input_tz = pytz.timezone(input_tzone)
    output_tz = pytz.timezone(output_tzone)
    
    # Creating datetime object for input_time in input_tzone
    naive_dt = datetime.strptime(input_time, "%Y-%m-%d %H:%M")
    aware_dt = input_tz.localize(naive_dt)
    
    # Converting the time to output_tzone
    converted_time = aware_dt.astimezone(output_tz)
    
    return converted_time