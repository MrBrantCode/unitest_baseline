"""
QUESTION:
Implement the function `crop_bout_intervals` that takes a list of detected bout timestamps as input and returns a list of cropped time intervals around each bout. The function should adhere to the following specifications:
- The input is a list of floats representing the timestamps (in seconds) of detected behavioral bouts.
- The output is a list of tuples, each containing the start and end timestamps of the cropped interval around a behavioral bout.
- The cropped intervals should be centered around each bout timestamp and have a duration of `PRE_INT_BT_S + POST_INT_BT_S` seconds.
- The start timestamp of each cropped interval should be rounded down to the nearest multiple of `DEF_DT`, and the end timestamp should be rounded up to the nearest multiple of `DEF_DT`.
"""

import math

def crop_bout_intervals(bout_timestamps, DEF_DT, PRE_INT_BT_S, POST_INT_BT_S):
    cropped_intervals = []
    for bout in bout_timestamps:
        start_time = math.floor((bout - PRE_INT_BT_S) / DEF_DT) * DEF_DT
        end_time = math.ceil((bout + POST_INT_BT_S) / DEF_DT) * DEF_DT
        cropped_intervals.append((start_time, end_time))
    return cropped_intervals