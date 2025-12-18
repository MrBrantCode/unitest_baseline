"""
QUESTION:
Design a function named `find_min_intervals` that takes a list of intervals as input and returns the minimum number of non-overlapping intervals needed to cover the entire range and the resulting new set of intervals. The input list of intervals can include negative integers and zeroes, with the start of any interval never being larger than the end of the same interval, and a maximum length of 10,000 intervals.
"""

def find_min_intervals(intervals):
    # Sort intervals by their start
    sorted_intervals = sorted(intervals, key=lambda x: x[0])

    merged = []

    for interval in sorted_intervals:
        # Check if this interval overlaps with the last one
        if merged and interval[0] <= merged[-1][1]:
            # If so, merge them by extending the last interval
            merged[-1][1] = max(merged[-1][1], interval[1])
        else:
            # Otherwise, add a new interval to our list
            merged.append(interval)

    # Return number of non-overlapping intervals and the intervals itself
    return len(merged), merged