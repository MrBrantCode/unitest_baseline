"""
QUESTION:
Write a function `find_max_overlapping_events(intervals)` that takes a list of intervals, where each interval is a list of two integers representing the start and end times, and returns a tuple containing the maximum number of overlapping events and the intervals at which they occur. The function should have a time complexity of O(n log n) to handle large input sizes efficiently.
"""

def find_max_overlapping_events(intervals):
    intervals.sort(key=lambda x: x[0])  # Sort intervals based on start times
    
    maxOverlap = 0
    currentOverlap = 0
    maxOverlappingIntervals = []
    overlappingIntervalsStack = []
    
    for interval in intervals:
        if not overlappingIntervalsStack:
            overlappingIntervalsStack.append(interval)
            currentOverlap = 1
        elif interval[0] <= overlappingIntervalsStack[-1][1]:
            overlappingIntervalsStack.append(interval)
            currentOverlap += 1
        else:
            if currentOverlap > maxOverlap:
                maxOverlap = currentOverlap
                maxOverlappingIntervals = overlappingIntervalsStack.copy()
            overlappingIntervalsStack.clear()
            overlappingIntervalsStack.append(interval)
            currentOverlap = 1
    
    if currentOverlap > maxOverlap:
        maxOverlap = currentOverlap
        maxOverlappingIntervals = overlappingIntervalsStack.copy()
    
    return maxOverlap, maxOverlappingIntervals