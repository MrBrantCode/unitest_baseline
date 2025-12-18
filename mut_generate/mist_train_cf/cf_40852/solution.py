"""
QUESTION:
Implement a function `max_non_overlapping_overpasses(overpasses)` that takes a list of overpasses as input, where each overpass is a tuple of two integers representing the start and end points of the overpass. The function should return the maximum number of non-overlapping overpasses that can be built. The input list of overpasses is not necessarily sorted, and the start and end points of an overpass are inclusive.
"""

from typing import List, Tuple

def maxNonOverlapping(overpasses: List[Tuple[int, int]]) -> int:
    if not overpasses:
        return 0
    
    overpasses.sort(key=lambda x: x[1])  # Sort overpasses based on end points
    
    count = 1  # Initialize count with 1 for the first overpass
    end = overpasses[0][1]  # Initialize end point with the end point of the first overpass
    
    for start, overpass_end in overpasses[1:]:
        if start > end:  # If the start point of the next overpass is greater than the current end point
            count += 1  # Increment count
            end = overpass_end  # Update end point
        
    return count