"""
QUESTION:
Write a function `merge_intervals(intervals)` that takes a sorted list of intervals, where each interval is a list of two integers `[start, end]`, and returns a new list of non-overlapping intervals. The function should merge overlapping intervals by updating the end value of the overlapping interval and add non-overlapping intervals to the result list.
"""

def entance(intervals):
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