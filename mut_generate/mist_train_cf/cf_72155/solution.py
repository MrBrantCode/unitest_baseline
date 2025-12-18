"""
QUESTION:
Given a set of non-overlapping intervals sorted by their start times, create a function `insert` that inserts a new interval into the intervals and merges overlapping intervals if necessary. The function should return the updated list of intervals and the number of intervals that were merged. 

The input intervals and the new interval are lists of two integers representing the start and end times, respectively. The function should handle cases where the new interval does not overlap with any existing interval, partially overlaps with one or more existing intervals, or completely overlaps with one or more existing intervals. The function should also handle edge cases such as an empty list of intervals or a new interval that is contained within an existing interval.

Constraints: 
- The input list of intervals can have up to 10^4 elements.
- Each interval is a list of two integers representing the start and end times, respectively.
- The start time of each interval is less than or equal to its end time.
- The input intervals are sorted by their start times in ascending order.
- The new interval is a list of two integers representing the start and end times, respectively.
- The start time of the new interval is less than or equal to its end time.
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

    return result, mergeCount-1 if mergeCount > 0 else 0