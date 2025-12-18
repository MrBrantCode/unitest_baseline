"""
QUESTION:
Implement a function `max_overlapping_intervals(intervals: List[Tuple[int, int]]) -> int` to find the maximum number of overlapping time intervals at any point in time. The input is a list of time intervals, where each interval is a tuple of two integers representing the start and end times. The function should return the maximum number of overlapping intervals. Assume that the input list is non-empty and the intervals are valid (i.e., the start time is less than or equal to the end time).
"""

from typing import List, Tuple

def max_overlapping_intervals(intervals: List[Tuple[int, int]]) -> int:
    events = []
    for start, end in intervals:
        events.append((start, 1))
        events.append((end, -1))
    events.sort()
    
    max_overlapping = 0
    current_overlapping = 0
    for _, event_type in events:
        current_overlapping += event_type
        max_overlapping = max(max_overlapping, current_overlapping)
    
    return max_overlapping