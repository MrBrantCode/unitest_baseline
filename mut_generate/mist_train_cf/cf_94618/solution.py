"""
QUESTION:
Find the maximum number of overlapping intervals in a given set of intervals. Each interval is represented by a pair of integers denoting its start and end points. Intervals that partially overlap should be considered. The input intervals may contain duplicates. The function should handle duplicates accordingly and return the actual intervals that have the maximum overlap.

The function, `findMaxOverlap(intervals)`, takes a list of intervals as input, where each interval is a tuple of two integers representing the start and end points. The function should return a tuple containing the maximum number of overlapping intervals and the actual intervals with the maximum overlap.
"""

def findMaxOverlap(intervals):
    # Sort the intervals based on start points and end points
    sortedIntervals = sorted(intervals, key=lambda x: (x[0], x[1]))

    # Initialize variables
    maxOverlap = 0
    maxOverlapIntervals = []
    stack = []

    # Push the first interval onto the stack
    stack.append(sortedIntervals[0])

    # Iterate through the sorted intervals
    for i in range(1, len(sortedIntervals)):
        currentInterval = sortedIntervals[i]
        topInterval = stack[-1]

        if currentInterval[0] > topInterval[1]:
            # No overlap, push current interval onto stack
            stack.append(currentInterval)
        elif currentInterval[1] <= topInterval[1]:
            # Complete overlap, discard top interval and push current interval onto stack
            stack.pop()
            stack.append(currentInterval)
        else:
            # Partial overlap, update maxOverlap and maxOverlapIntervals if necessary
            overlap = topInterval[1] - currentInterval[0] + 1
            if overlap > maxOverlap:
                maxOverlap = overlap
                maxOverlapIntervals = [topInterval, currentInterval]

    return maxOverlap, maxOverlapIntervals