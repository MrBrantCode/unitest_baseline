"""
QUESTION:
Note: This POTD is a part of Geek Summer Carnival. Solve all POTD consecutively from 5th to 10th April and get a chance to win exclusive discount vouchers on our GfG courses.
Geek wants to select the maximum number of course bundles at the Geek Summer Carnival. 
You are given a finite number of courses and N range of numbers each depicting a bundle of courses. Select the maximum number of bundles such that no courses overlap in any of the bundle.
Note: The ending of a range being the same as start of another isn't considered as an overlap.
Example 1:
Input:
N = 4
Bundles = 
1 5
2 3
1 8
3 5
Output:
2
Explanation: 
We can select 2 bundles at max while 
staying true to the condition. For this, 
we can pick the ranges (2,3) and (3,5) 
without any overlap. 
 
Example 2:
Input:
N = 5
Bundles = 
7 9 
2 8 
1 3 
10 11 
10 16
Output:
3
Explanation: 
We can pick the ranges (1,3), 
(7,9) and (10,11) without any overlap.
Your Task:
You don't need to read input or print anything. Complete the function max_non_overlapping() that takes a 2D array representing N ranges as input parameter.  Return the maximum number of course bundles. 
Expected time complexity: O(NlogN)
Expected space complexity: O(1)
Constraints:
1 <= N <= 1000
0 <= range[i][j] <= 1000
"""

def max_non_overlapping_bundles(ranges):
    # Sort the ranges by their end times, and then by their start times
    ranges.sort(key=lambda x: (x[1], x[0]))
    
    # Initialize the count of non-overlapping bundles and the end time of the last selected bundle
    count = 0
    prev_end = -1
    
    # Iterate through each range
    for r in ranges:
        # If the start of the current range is greater than or equal to the end of the last selected range
        if r[0] >= prev_end:
            # Select this range
            count += 1
            # Update the end time of the last selected range
            prev_end = r[1]
    
    # Return the maximum number of non-overlapping bundles
    return count