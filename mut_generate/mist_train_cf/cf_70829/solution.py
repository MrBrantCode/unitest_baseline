"""
QUESTION:
Design a method `min_intervals` that determines the minimum number of non-overlapping intervals needed to cover the entire range of a set of intervals. The method should take a 2D list of intervals as input, where each interval is a list of two integers representing the start and end times. The method should return the minimum number of non-overlapping intervals required.
"""

def min_intervals(intervals):
    if not intervals:
        return 0
        
    # Sort intervals by end time
    intervals.sort(key=lambda x: x[1])
    
    # Initialize the end time of the first interval
    end = intervals[0][1]
    count = 1
    
    for i in range(1, len(intervals)):
        # If the start time of the current interval is greater than or equal to the end time of 
        # the previous interval, then it is not overlapping. 
        if intervals[i][0] >= end:
            # Update end time and count
            end = intervals[i][1]
            count += 1

    return count