"""
QUESTION:
Write a Python function `total_duration` that takes a list of time intervals as input, where each interval is a tuple of two integers representing the start and end times. The function should return the total duration covered by all the intervals, handling overlapping intervals. The input list `tl_list` is a list of tuples in the format `(start_time, end_time)`.
"""

def total_duration(tl_list):
    if not tl_list:
        return 0

    # Sort the intervals based on their start times
    sorted_intervals = sorted(tl_list, key=lambda x: x[0])

    total_duration = 0
    current_start, current_end = sorted_intervals[0]

    for start, end in sorted_intervals[1:]:
        if start <= current_end:  # Overlapping intervals
            current_end = max(current_end, end)
        else:
            total_duration += current_end - current_start
            current_start, current_end = start, end

    total_duration += current_end - current_start  # Add the duration of the last interval
    return total_duration