"""
QUESTION:
Write a function `timestamp_diff` that takes two Unix timestamps as input, representing the number of seconds since January 1, 1970, and returns their difference in minutes, rounded down to the nearest whole number. The timestamps can range from 0 to 10^9. Implement the solution without using built-in date or time libraries. The time complexity should be O(1).
"""

def timestamp_diff(timestamp1, timestamp2):
    diff = abs(timestamp1 - timestamp2)  
    diff_minutes = diff // 60  
    return diff_minutes