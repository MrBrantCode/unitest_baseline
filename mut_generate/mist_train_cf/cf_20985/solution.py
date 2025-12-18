"""
QUESTION:
Write a function named `merge_intervals` that merges overlapping intervals in a given list of intervals. The function should take a list of intervals as input, where each interval is a list of two integers representing the start and end times. The function should return a new list of merged intervals. 

The function should have a time complexity of O(n log n) and a space complexity of O(n), where n is the number of intervals in the input list.
"""

def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort based on start time
    result = [intervals[0]]
    for i in range(1, len(intervals)):
        if intervals[i][0] <= result[-1][1]:  
            result[-1][1] = max(intervals[i][1], result[-1][1])
        else:
            result.append(intervals[i])
    return result