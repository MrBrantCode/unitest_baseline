"""
QUESTION:
Implement a function named `timestamp_diff` that takes two Unix timestamps `timestamp1` and `timestamp2` as input, both in the range of 0 to 10^9, and returns the absolute difference between them in minutes, rounded down to the nearest whole number. The function should not use any built-in date or time libraries and have a time complexity of O(1).
"""

def timestamp_diff(timestamp1, timestamp2):
    diff = abs(timestamp1 - timestamp2)  
    diff_minutes = diff // 60  
    return diff_minutes