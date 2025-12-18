"""
QUESTION:
Write a function `find_max_overlap(intervals)` that finds the maximum number of overlapping intervals and the actual intervals with the maximum overlap in a given set of intervals. 

The function takes a list of intervals as input, where each interval is a list of two integers representing the start and end points of the interval. The function should consider intervals that partially overlap as well and handle duplicate intervals. 

The function should return a tuple containing the maximum number of overlapping intervals and the actual intervals with the maximum overlap. The function should have a time complexity of O(nlogn) and use O(1) space complexity, excluding the space needed for the input and output.
"""

def find_max_overlap(intervals):
    # Sort the intervals based on start points and end points
    intervals.sort(key=lambda x: (x[0], x[1]))

    maxOverlap = 0
    currentOverlap = 0
    maxOverlapIntervals = []

    # Iterate through the sorted intervals
    for i in range(len(intervals)):
        if i > 0 and intervals[i][0] <= intervals[i-1][1]:
            # If the current interval overlaps with the previous interval
            currentOverlap += 1
        else:
            # If the current interval does not overlap with the previous interval
            if currentOverlap > maxOverlap:
                # Update maxOverlap and maxOverlapIntervals
                maxOverlap = currentOverlap
                maxOverlapIntervals = intervals[i-currentOverlap:i]
            currentOverlap = 1

    # Handle the case when the last interval has the maximum overlap
    if currentOverlap > maxOverlap:
        maxOverlap = currentOverlap
        maxOverlapIntervals = intervals[len(intervals)-currentOverlap:]

    return maxOverlap, maxOverlapIntervals