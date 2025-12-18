"""
QUESTION:
Write a function `maxOverlaps(intervals)` that takes a list of intervals as input where each interval is a list of two integers representing the start and end points of the interval. The function should return the maximum number of overlapping intervals. The input list can be empty, and the intervals in the list are not guaranteed to be in any particular order. The function should assume that the intervals are closed, i.e., the end points are included in the intervals.
"""

def maxOverlaps(intervals): 
    if len(intervals) == 0: 
        return 0

    intervals.sort(key = lambda x: x[0])
    result = [0] * len(intervals) 
    result[0] = 1
    endpoint = intervals[0][1] 

    for i in range(1, len(intervals)): 
        if intervals[i][0] <= endpoint: 
            result[i] = result[i - 1] + 1
        else: 
            result[i] = 1
        endpoint = max(endpoint, intervals[i][1]) 

    return max(result)