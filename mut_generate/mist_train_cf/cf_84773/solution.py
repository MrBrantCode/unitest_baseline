"""
QUESTION:
Write a function `maxOverlapping(intervals)` that takes a list of intervals where each interval is a list of two integers representing the start and end times. The function should return the maximum number of overlapping intervals. The intervals can be overlapping if the start time of one interval is less than or equal to the end time of the other interval.
"""

import heapq

def maxOverlapping(intervals):
    # Sort the intervals based on their start times
    intervals.sort()

    # Initialize a priority queue with the end time of the first interval
    heap, maxOverlap = [intervals[0][1]], 1

    # For each remaining interval
    for start, end in intervals[1:]:
        # While there is some overlap
        while heap and heap[0] <= start:
            # Remove the interval from the heap
            heapq.heappop(heap)
                
        # Add the end time of the current interval to the heap
        heapq.heappush(heap, end)
            
        # Update the maximum number of overlaps
        maxOverlap = max(maxOverlap, len(heap))
        
    # Return the maximum overlap
    return maxOverlap