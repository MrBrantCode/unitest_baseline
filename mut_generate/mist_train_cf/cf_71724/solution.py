"""
QUESTION:
Create a function `convert_to_jst` that takes two parameters: `time` and `timezone_str`, where `time` is the current time in any of the 24 global time zones and `timezone_str` is a string representing the time zone in the format "Area/City" (e.g., "America/New_York", "Europe/Paris", etc.). The function should return the time in Japanese Standard Time (JST) in the format "YYYY-MM-DD HH:MM:SS JST+0900". The function should handle daylight saving time where applicable.
"""

from datetime import datetime
from pytz import timezone
import pytz

def convert_to_jst(time, timezone_str):
    local_tz = pytz.timezone(timezone_str)
    local_dt = local_tz.localize(time, is_dst=None)
    jst_tz = timezone('Asia/Tokyo')
    jst_dt = local_dt.astimezone(jst_tz)

    return jst_dt.strftime('%Y-%m-%d %H:%M:%S %Z%z')