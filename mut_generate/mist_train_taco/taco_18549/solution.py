"""
QUESTION:
Given a collection of Intervals, the task is to merge all of the overlapping Intervals.
Example 1:
Input:
Intervals = {{1,3},{2,4},{6,8},{9,10}}
Output: {{1, 4}, {6, 8}, {9, 10}}
Explanation: Given intervals: [1,3],[2,4]
[6,8],[9,10], we have only two overlapping
intervals here,[1,3] and [2,4]. Therefore
we will merge these two and return [1,4],
[6,8], [9,10].
Example 2:
Input:
Intervals = {{6,8},{1,9},{2,4},{4,7}}
Output: {{1, 9}}
Your Task:
Complete the function overlappedInterval() that takes the list N intervals as input parameters and returns sorted list of intervals after merging.
Expected Time Complexity: O(N*Log(N)).
Expected Auxiliary Space: O(Log(N)) or O(N).
Constraints:
1 ≤ N ≤ 100
0 ≤ x ≤ y ≤ 1000
"""

def merge_intervals(intervals):
    if not intervals:
        return []
    
    # Sort intervals based on the start time
    intervals.sort()
    
    merged_intervals = []
    current_start, current_end = intervals[0]
    
    for start, end in intervals[1:]:
        if start <= current_end:
            # There is an overlap, merge the intervals
            current_end = max(current_end, end)
        else:
            # No overlap, add the current interval to the result
            merged_intervals.append((current_start, current_end))
            current_start, current_end = start, end
    
    # Add the last interval
    merged_intervals.append((current_start, current_end))
    
    return merged_intervals