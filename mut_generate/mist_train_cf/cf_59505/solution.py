"""
QUESTION:
Given a collection of intervals where each interval is a list of two integers representing the start and end points, find the minimum number of intervals to remove to make the rest of the intervals non-overlapping. The intervals cannot be rearranged, and it is guaranteed that the end point of an interval is always greater than its start point. Intervals with touching borders are not considered overlapping.
"""

def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0
    intervals.sort(key=lambda interval: interval[1])
    prev_end = intervals[0][1]
    count = 0
    for interval in intervals[1:]:
        if interval[0] < prev_end: 
            count += 1
        else: 
            prev_end = interval[1]
    return count