"""
QUESTION:
Design an algorithm to find the largest subset of non-overlapping intervals that maximizes their total length. Implement a function named `select_intervals` that takes a list of intervals as input, where each interval is represented as a pair of begin and end times, with the begin time included and the end time excluded. The function should return a list of non-overlapping intervals in the same format.
"""

def select_intervals(intervals):
    intervals.sort(key=lambda x: x[1])  # Sort by end time
    
    selected = []
    for interval in intervals:
        if not selected or interval[0] >= selected[-1][1]:
            selected.append(interval)
    
    return selected