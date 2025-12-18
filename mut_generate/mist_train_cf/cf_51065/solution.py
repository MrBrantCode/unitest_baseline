"""
QUESTION:
Create a function named `max_overlapping_and_remaining_intervals` that takes a list of unique intervals `intervals` as input where `1 <= intervals.length <= 1000` and `intervals[i].length == 2`. Each interval is represented as a list of two integers `[start, end]` where `0 <= start < end <= 10^5`. The function should return a tuple of two integers where the first integer represents the number of intervals remaining after removing all intervals that are covered by another interval in the list, and the second integer represents the maximum number of overlapping intervals at any point in time.
"""

def max_overlapping_and_remaining_intervals(intervals):
    intervals.sort(key=lambda x: (x[0], -x[1]))
    max_end, removed = -1, 0
    for start, end in intervals:
        if end <= max_end:
            removed += 1
        else:
            max_end = end
    remaining = len(intervals) - removed

    intervals.sort()
    max_overlapping = active_intervals = 0
    j = 0
    for i in range(len(intervals)):
        while j < len(intervals) and intervals[j][0] < intervals[i][1]:
            active_intervals += 1
            j += 1
        max_overlapping = max(max_overlapping, active_intervals)
        while j < len(intervals) and intervals[j][0] >= intervals[i][1]:
            active_intervals -= 1
            j += 1

    return (remaining, max_overlapping)