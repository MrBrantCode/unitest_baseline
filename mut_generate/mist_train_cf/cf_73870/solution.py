"""
QUESTION:
Write a function `convert_time(jst_time, utc_offset)` that takes a time string `jst_time` in Japan Standard Time (JST, UTC+9) in the format 'YYYY-MM-DD HH:MM:SS' and an integer `utc_offset` representing the UTC offset of the target timezone. The function should return the time string in the target timezone, handling conversions across different days.
"""

from datetime import datetime, timedelta

def convert_time(jst_time, utc_offset):
    jst_offset = 9
    jst_time_obj = datetime.strptime(jst_time, '%Y-%m-%d %H:%M:%S')
    new_time_obj = jst_time_obj + timedelta(hours=utc_offset - jst_offset)
    new_time = new_time_obj.strftime('%Y-%m-%d %H:%M:%S')
    return new_time