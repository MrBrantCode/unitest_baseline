"""
QUESTION:
Write a function `merge_intervals(intervals)` that takes a list of intervals, where each interval is a list of two integers `[start, end]`, and returns a new list of non-overlapping intervals. The function should merge any overlapping intervals in the input list. The intervals in the input list are not guaranteed to be sorted, and the function should be able to handle an empty input list.
"""

def merge_intervals(intervals):
    if not intervals:
        return []

    intervals.sort(key=lambda x: x[0])  # Sort intervals based on the start value

    merged = [intervals[0]]  # Initialize the merged list with the first interval

    for interval in intervals[1:]:
        if merged[-1][1] >= interval[0]:  # Check for overlap
            merged[-1][1] = max(merged[-1][1], interval[1])  # Merge the intervals
        else:
            merged.append(interval)  # Add non-overlapping interval to the merged list

    return merged