"""
QUESTION:
Write a function `find_max_overlapping_intervals` that takes a list of intervals as input where each interval is a pair of integers representing its start and end points. The function should return the maximum number of overlapping intervals. The intervals may contain duplicates and partial overlaps are considered overlaps. The input list can be modified in-place.
"""

def find_max_overlapping_intervals(intervals):
    intervals.sort(key=lambda x: (x[0], x[1]))  # Sort intervals based on start points and end points
    
    maxOverlaps = 0
    currentOverlaps = 1
    previousEnd = intervals[0][1]
    
    for i in range(1, len(intervals)):
        currentStart, currentEnd = intervals[i]
        
        if currentStart <= previousEnd:
            currentOverlaps += 1
        else:
            maxOverlaps = max(maxOverlaps, currentOverlaps)
            currentOverlaps = 1
        
        previousEnd = max(previousEnd, currentEnd)
    
    maxOverlaps = max(maxOverlaps, currentOverlaps)
    return maxOverlaps