"""
QUESTION:
Write a Python function `get_unique_values` that takes a collection of numerical intervals as input, where each interval is a tuple of two integers, and returns a list of distinct integers within these intervals.
"""

def get_unique_values(intervals):
    unique = set()
    for interval in intervals:
        for num in range(interval[0], interval[1]+1):
            unique.add(num)
    return sorted(list(unique))