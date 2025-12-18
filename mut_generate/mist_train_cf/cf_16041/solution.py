"""
QUESTION:
Write a function `convert_utc_to_local` that takes two parameters: `utc_time_str` and `timezone_str`. The function should convert the UTC time represented by `utc_time_str` to the local time in the specified `timezone_str`. The function should handle invalid input formats by catching `ValueError` exceptions and printing "Invalid input format." The input `utc_time_str` is in the format "%Y-%m-%d %H:%M:%S". The function should return the local time in the same format.
"""

from datetime import datetime
import pytz

def convert_utc_to_local(utc_time_str, timezone_str):
    try:
        utc_time = datetime.strptime(utc_time_str, "%Y-%m-%d %H:%M:%S")
        timezone = pytz.timezone(timezone_str)
        local_time = utc_time.replace(tzinfo=pytz.utc).astimezone(timezone)
        return local_time.strftime("%Y-%m-%d %H:%M:%S")
    except ValueError:
        print("Invalid input format.")
        return None