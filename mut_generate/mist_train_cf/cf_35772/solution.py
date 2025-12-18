"""
QUESTION:
Write a function `merge_intervals(intervals)` that takes in a list of intervals, where each interval is a list of two integers representing the start and end points of the interval. The function should merge overlapping intervals and return a new list of non-overlapping intervals, sorted by the start value of the intervals. The function should handle an empty list of intervals and return an empty list. The function should assume that the input intervals are valid and the start value is less than or equal to the end value in each interval.
"""

from typing import List

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])  

    merged = [intervals[0]]  

    for interval in intervals[1:]:
        if interval[0] <= merged[-1][1]:  
            merged[-1][1] = max(merged[-1][1], interval[1])  
        else:
            merged.append(interval)  

    return merged