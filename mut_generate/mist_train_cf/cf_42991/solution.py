"""
QUESTION:
Write a function `merge_intervals(intervals)` that takes in a list of intervals, where each interval is a list of two non-negative integers `[start, end]` with `start` less than `end`, and returns a new list of non-overlapping intervals after merging overlapping intervals. The input list is non-empty and intervals may overlap and are not sorted.
"""

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])  

    result = [intervals[0]]  
    for interval in intervals[1:]:
        if interval[0] <= result[-1][1]:  
            result[-1][1] = max(result[-1][1], interval[1])  
        else:
            result.append(interval)  

    return result