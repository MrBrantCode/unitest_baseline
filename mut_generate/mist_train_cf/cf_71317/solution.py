"""
QUESTION:
Design a function named `min_intervals` that determines the minimum number of non-overlapping intervals needed to cover the entire range of a set of intervals. The function should take a list of intervals as input, where each interval is represented as a list of two numbers, the start and end points. The function should handle fractional numbers and intervals with the same start/end points. The function should return the minimum number of non-overlapping intervals required.
"""

def min_intervals(intervals):
    if not intervals:  
        return 0  

    intervals.sort(key=lambda x: (x[0], -x[1]))  
   
    last_end = intervals[0][1]
    count = 1
   
    for start, end in intervals[1:]:
        # Only increment the count 
        # if this interval does not overlap with the last one
        if start > last_end:  
            count += 1
            last_end = end
            
        # If there is an overlap, make sure that
        # we choose the interval with the larger end time
        elif end > last_end:  
            last_end = end
            
    return count