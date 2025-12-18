"""
QUESTION:
Design a function `select_intervals(intervals)` that takes a list of intervals, where each interval is represented as a pair of begin and end times, and returns the largest subset of non-overlapping intervals that maximizes their total length. The intervals can be open or closed, and the function should use a heuristic approach to minimize the search space and runtime complexity.
"""

def select_intervals(intervals):
    intervals.sort(key=lambda x: x[1])  # Sort by end time
    selected = []
    for interval in intervals:
        if not selected or interval[0] >= selected[-1][1]:
            selected.append(interval)
    return selected