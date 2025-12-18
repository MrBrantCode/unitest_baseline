"""
QUESTION:
Design a method named `minimum_intervals` that takes a list of intervals as input, where each interval is a list of two integers representing the start and end time of the interval. The method should return the minimum number of non-overlapping intervals needed to cover the entire range of the input intervals. If there are multiple optimal solutions, the method should return any one of them. The intervals may overlap but not completely cover each other.
"""

def minimum_intervals(intervals):
    # Sort intervals by start seconds
    intervals.sort(key=lambda interval: interval[0])

    # Initialize variables
    res = []
    end = float('-inf')

    # Iterate through the sorted list of intervals
    for interval in intervals:
        # If current interval does not overlap with previous one, append it to the result
        if interval[0] > end:
            res.append(interval)
            end = interval[1]
        # If current interval overlaps with previous one but ends later, update the end time of the last interval in result
        elif interval[1] > end:
            res[-1][1] = interval[1]
            end = interval[1]

    return res