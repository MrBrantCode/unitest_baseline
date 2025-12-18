"""
QUESTION:
Develop a function named `convert_time` that takes two string arguments, `mst_time_str` and `target_tz_str`, where `mst_time_str` represents a date and time in the format "YYYY-MM-DD HH:MM" in Mountain Standard Time (MST) and `target_tz_str` is the target timezone to which the date and time should be converted. The function should return the date and time in both MST and the target timezone, along with the day of the week for each, while handling daylight saving time changes. The function should also include error handling for invalid date, time, and timezone inputs.
"""

from datetime import datetime
from pytz import timezone, UnknownTimeZoneError

def convert_time(mst_time_str, target_tz_str):
    try:
        mst_tz = timezone('America/Denver')  
        target_tz = timezone(target_tz_str)  

        mst_time = datetime.strptime(mst_time_str, '%Y-%m-%d %H:%M')
        mst_time = mst_tz.localize(mst_time, is_dst=None)
        mst_day_of_week = mst_time.strftime('%A')  

        target_time = mst_time.astimezone(target_tz)
        target_day_of_week = target_time.strftime('%A')  

        return (mst_time.strftime('%Y-%m-%d %H:%M') + ' ' + mst_day_of_week, 
                target_time.strftime('%Y-%m-%d %H:%M') + ' ' + target_day_of_week)

    except (ValueError, UnknownTimeZoneError) as e:
        return "Error: Invalid date, time, or timezone."