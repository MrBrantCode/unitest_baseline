"""
QUESTION:
Given a list of intervals where each interval is a pair of integers [start, end], write a function `min_intervals` that returns the minimum number of intervals required to cover all the given intervals. The intervals may overlap. The function should take a list of intervals as input and return an integer.

Restriction: The input list will contain at least one interval.
"""

from typing import List

def min_intervals(intervals: List[List[int]]) -> int:
    intervals.sort(key=lambda x: x[1])  
    count = 1  
    end = intervals[0][1]  

    for a, b in intervals[1:]:
        if a > end:  
            count += 1  
            end = b  

    return count