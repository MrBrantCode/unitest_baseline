"""
QUESTION:
Develop a function `find_max_overlapping_events` that takes a list of intervals as input, where each interval is a list of two integers representing the start and end times. Each event has a minimum duration of 2 units of time. The function should return the maximum number of overlapping events and the intervals at which they occur. The function should have a time complexity of O(n log n), where n is the number of intervals.
"""

def find_max_overlapping_events(intervals):
    intervals.sort(key=lambda x: x[0])  
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