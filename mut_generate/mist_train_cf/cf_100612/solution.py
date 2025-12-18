"""
QUESTION:
Write a function `time_diffs` that takes a list of timestamps in `hh:mm:ss` format and returns a list of integers representing the differences in seconds between adjacent timestamps. The function should use a single list comprehension, without any explicit loops, and with a time complexity not exceeding O(1) for built-in functions and external libraries.
"""

from datetime import datetime

def time_diffs(timestamps):
    return [int((datetime.strptime(t2, '%H:%M:%S') - datetime.strptime(t1, '%H:%M:%S')).total_seconds()) 
            for t1, t2 in zip(timestamps, timestamps[1:])]