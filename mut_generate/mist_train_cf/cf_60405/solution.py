"""
QUESTION:
Write a function `convert_time(london_time, is_dst)` that takes a string `london_time` representing a time in London Time (GMT) in "HH:MM" format and a boolean `is_dst` indicating whether it's Daylight Saving Time in New Zealand. The function should convert the given time to New Zealand Standard Time (NZST) and return the converted time as a string in "HH:MM" format, handling the case when the time passes midnight and accounting for Daylight Saving Time.
"""

def convert_time(london_time, is_dst=False):
    hours, minutes = map(int, london_time.split(':'))
    nz_time = (hours + 12) % 24
    if is_dst:
        nz_time = (nz_time + 1) % 24

    nz_time_str = "{0:02d}:{1:02d}".format(nz_time, minutes)
    return nz_time_str