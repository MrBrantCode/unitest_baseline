"""
QUESTION:
Given a collection of intervals where each interval is represented as a list of two integers, write a function `merge(intervals)` that merges all overlapping intervals. The function should return a list of merged intervals. 

Assume that the end point of each interval is always bigger than its start point, and intervals like [1,2] and [2,3] do not overlap because their borders are only touching. The input intervals are not guaranteed to be sorted.
"""

def merge(intervals):
    result = []
    if intervals:
        intervals.sort()
        result.append(intervals[0])

        for i in range(1, len(intervals)):
            if result[-1][1] >= intervals[i][0]:
                result[-1][1] = max(result[-1][1], intervals[i][1])
            else:
                result.append(intervals[i])

    return result