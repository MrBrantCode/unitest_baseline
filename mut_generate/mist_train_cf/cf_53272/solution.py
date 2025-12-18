"""
QUESTION:
Write a function `convert_time` that takes three parameters: `input_time` in the format 'YYYY-MM-DD HH:MM', `input_tz`, and `output_tz`. The function should convert the `input_time` from the `input_tz` timezone to the `output_tz` timezone, handling daylight saving times and non-standard time zones. The function should also handle faulty inputs and return an error message in case of incorrect data entry for the time and/or timezone. The `input_tz` and `output_tz` should be valid timezones as per the pytz library.
"""

import pytz
from datetime import datetime

def convert_time(input_time, input_tz, output_tz):
    try:
        # Parse time
        parsed_time = datetime.strptime(input_time, '%Y-%m-%d %H:%M')

        # Set the timezone to the input timezone
        old_tz = pytz.timezone(input_tz)
        old_tz_time = old_tz.localize(parsed_time)

        # Convert to the desired timezone
        new_tz = pytz.timezone(output_tz)
        new_tz_time = old_tz_time.astimezone(new_tz)
        return new_tz_time.strftime('%Y-%m-%d %H:%M')

    except Exception as e:
        # Handle exceptions, most likely because of wrong input
        return repr(e)