"""
QUESTION:
Implement a function `merge_intervals(intervals)` that takes a list of intervals, where each interval is a list of two integers representing the start and end times, and returns a new list of merged intervals. The function should merge overlapping intervals and return the resulting list of non-overlapping intervals.

Restrictions: 
- The input list of intervals is not sorted.
- The start time of an interval is less than or equal to its end time.
- The input list can contain duplicate intervals or intervals with zero duration.
- The function should return a new list of merged intervals, without modifying the original input list.
"""

def merge_intervals(intervals):
    """
    This function merges overlapping intervals and returns a new list of non-overlapping intervals.

    Args:
        intervals (list): A list of intervals, where each interval is a list of two integers representing the start and end times.

    Returns:
        list: A new list of merged intervals.
    """

    # Sort the input list of intervals based on the start time
    intervals.sort(key=lambda x: x[0])

    # Initialize an empty list, "result", to store the merged intervals
    result = [intervals[0]]

    # Iterate through each interval in the sorted list
    for i in range(1, len(intervals)):
        # If the current interval's start time is greater than the end time of the last interval in "result", 
        # add the current interval to "result"
        if intervals[i][0] > result[-1][1]:
            result.append(intervals[i])
        # Otherwise, update the end time of the last interval in "result" to the maximum of the current interval's end time 
        # and the end time of the last interval in "result"
        else:
            result[-1][1] = max(intervals[i][1], result[-1][1])

    # Return the "result" list
    return result