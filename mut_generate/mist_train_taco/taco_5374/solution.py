"""
QUESTION:
Given a collection of intervals, merge all overlapping intervals.

Example 1:


Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].


Example 2:


Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.
"""

def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Sort intervals based on the start value
    intervals.sort(key=lambda x: x[0])
    
    merged = []
    current_start, current_end = intervals[0]
    
    for start, end in intervals[1:]:
        if start <= current_end:
            # Overlapping intervals, adjust the end
            current_end = max(current_end, end)
        else:
            # Non-overlapping interval, add the previous interval and reset bounds
            merged.append([current_start, current_end])
            current_start, current_end = start, end
    
    # Add the last interval
    merged.append([current_start, current_end])
    
    return merged