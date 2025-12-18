"""
QUESTION:
Given an 2D array intervals of size N representing intervals where intervals [ i ] = [start_{i} , end_{i }), return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.
 
Example 1:
Input:
N = 4
intervals [ ] = {{1, 2}, {2, 3}, {3, 4}, {1, 3}}
Output: 1
Explanation: 
{1, 3} can be removed and the rest of the intervals are non-overlapping.
 
Example 2:
Input:
N = 3
intervals [ ] = {{1, 3}, {1, 3}, {1, 3}}
Output: 2
Explanation: 
You need to remove two {1, 3} to make the rest of the intervals non-overlapping.
 
Your Task:
You don't need to read input or print anything. Your task is to complete the function minRemoval() which takes the interger N and 2D integer array intervals [ ] as parameters and returns the minimum number of intervals needs to remove in order to make the remaining intervals non-overlapping.
Expected Time Complexity: O(NlogN)
Expected Auxiliary Space: O(1)
Constraints:
1 ≤ N ≤  10^{5}
|intervals_{i}| == 2
-5*10^{4 }≤ start_{i }< end_{i} <=5*10^{4}
"""

def min_removal(N, intervals):
    # Sort intervals based on the end time
    intervals.sort(key=lambda i: i[1])
    
    # Initialize variables
    end = intervals[0][1]
    count = 0
    
    # Iterate through the intervals starting from the second one
    for i in range(1, N):
        if intervals[i][0] < end:
            # If the current interval overlaps with the previous one, increment the count
            count += 1
        else:
            # Update the end time to the current interval's end time
            end = intervals[i][1]
    
    return count