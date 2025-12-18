"""
QUESTION:
Insert the new interval into the list of non-overlapping intervals sorted by their start times, merging any overlapping intervals if necessary. 

The function `insert_interval` takes a list of intervals and a new interval as input. The intervals are given as a list of lists, where each sublist contains two integers representing the start and end times of an interval. The function should return the updated list of intervals after the new interval has been inserted and merged if necessary. 

Restrictions: 
- The list of intervals is sorted by their start times.
- The intervals in the list are non-overlapping.
"""

from typing import List

def insert_intervals(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    merged = []
    i = 0
    n = len(intervals)
    
    # Add all intervals that come before the new interval
    while i < n and intervals[i][1] < new_interval[0]:
        merged.append(intervals[i])
        i += 1
    
    # Merge overlapping intervals
    while i < n and intervals[i][0] <= new_interval[1]:
        new_interval[0] = min(new_interval[0], intervals[i][0])
        new_interval[1] = max(new_interval[1], intervals[i][1])
        i += 1
    
    merged.append(new_interval)
    
    # Add all intervals that come after the new interval
    while i < n:
        merged.append(intervals[i])
        i += 1
    
    return merged