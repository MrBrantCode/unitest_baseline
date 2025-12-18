"""
QUESTION:
Write a function called `diffs` that takes a list of strings representing timestamps in `hh:mm:ss` format and returns a list of integers representing the differences in seconds between adjacent timestamps. The function should use a single list comprehension and not exceed a time complexity of O(1) for built-in functions and external libraries. No loops are allowed.
"""

from datetime import datetime

def diffs(timestamps):
    return [int((datetime.strptime(t2, '%H:%M:%S') - datetime.strptime(t1, '%H:%M:%S')).total_seconds()) 
            for t1, t2 in zip(timestamps, timestamps[1:])]