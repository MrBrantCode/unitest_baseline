"""
QUESTION:
Implement a function named `insert` that takes two parameters: a list of intervals (`intervals`) and a new interval (`newInterval`). The function should insert the `newInterval` into the list of `intervals` and merge any overlapping intervals. The function should return a list of merged intervals and the number of intervals that were merged.

Each interval is represented as a list of two integers, `[start, end]`. The input list of intervals is sorted by their start value. The function should return a new list of merged intervals, also sorted by their start value, and the count of merged intervals (or 0 if no intervals were merged).

Example: `insert([[1,3],[6,9]], [2,5])` should return `([[1,5],[6,9]], 1)`.
"""

def insert(intervals, newInterval):
    result, mergeCount = [], 0
    i, n = 0, len(intervals)
    
    while i < n and intervals[i][1] < newInterval[0]: 
        result.append(intervals[i])
        i += 1

    while i < n and intervals[i][0] <= newInterval[1]: 
        newInterval = [min(intervals[i][0], newInterval[0]), max(intervals[i][1], newInterval[1])] 
        i += 1
        mergeCount += 1

    result.append(newInterval)
    while i < n:  
        result.append(intervals[i])
        i += 1

    return result, mergeCount - 1 if mergeCount > 0 else 0