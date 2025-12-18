"""
QUESTION:
Create a function `determine_overlapping_intervals(intervals)` that takes a list of intervals (tuples of two integers each) as input, where each interval represents a range of time, and returns a list of non-overlapping intervals by merging the overlapping ones. The intervals should be sorted based on their start times before merging. The function should be able to handle any number of intervals and any range of time.
"""

def determine_overlapping_intervals(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start time
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        previous = merged[-1]
        if current[0] <= previous[1]:  # Check for overlap
            merged[-1] = (previous[0], max(previous[1], current[1]))  # Merge overlapping intervals
        else:
            merged.append(current)
    
    return merged