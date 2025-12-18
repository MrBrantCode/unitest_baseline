"""
QUESTION:
Given N intervals of the form [A, B]. The task is to return the maximum number of overlap among these intervals at any time.
Example 1:
Input:
N = 3
Intervals[] = {{1, 2}, {2, 4}, {3, 6}}
Output: 
2
Explanation: 
The maximum overlapping is 2(between (1 2) and 
(2 4) or between (2 4) and (3 6)) 
Example 2:
Input:
N = 4
Intervals[] = {{1, 8}, {2, 5}, {5, 6}, {3, 7}}
Output: 
4
Explanation: 
The maximum overlapping is 4 (between (1, 8), 
(2, 5), (5, 6) and (3, 7))
 
Your Task:  
You don't need to read input or print anything. Your task is to complete the function overlap() which takes a list of pairs as input and returns an integer as output.
 
Expected Time Complexity: O(N * log N)
Expected Auxiliary Space: O(N)
 
Constraints:
2 <= N <= 2 * 10^{4}
1<= intervals[i][0] < intervals[i][1] <= 4*10^{3}
"""

from typing import List

def max_overlap(intervals: List[List[int]]) -> int:
    if not intervals:
        return 0
    
    beginnings = sorted([i[0] for i in intervals])
    endings = sorted([i[1] for i in intervals])
    
    max_overlap_count = 0
    current_overlap_count = 0
    i, j = 0, 0
    
    while i < len(beginnings) and j < len(endings):
        if beginnings[i] < endings[j]:
            current_overlap_count += 1
            max_overlap_count = max(max_overlap_count, current_overlap_count)
            i += 1
        else:
            current_overlap_count -= 1
            j += 1
    
    return max_overlap_count