"""
QUESTION:
Implement the `merge` function which takes an array of intervals, where each interval `intervals[i]` is a sub-array consisting of two elements `[starti, endi]`, and returns an array of the non-overlapping intervals that encompass all the intervals in the original input. The function should merge all overlapping intervals and return the merged intervals. 

The length of `intervals` is at least 1 and at most 10^4. Each `intervals[i]` has exactly 2 elements. The values of `starti` and `endi` are non-negative and do not exceed 10^4, with `starti` always being less than or equal to `endi`.
"""

def merge(intervals):
    # Sort the intervals by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    
    for i in intervals:
        # If the list of merged intervals is empty or if the current
        # interval does not overlap with the previous, append it.
        if not merged or merged[-1][1] < i[0]:
            merged.append(i)
        else:
            # Otherwise, there is overlap, so we merge the current and previous
            # intervals by updating the end of the previous interval with the max end time.
            merged[-1][1] = max(merged[-1][1], i[1])
    
    return merged