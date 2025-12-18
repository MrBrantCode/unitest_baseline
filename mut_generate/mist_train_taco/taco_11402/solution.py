"""
QUESTION:
Given an integer n. Each number from 1 to n is grouped according to the sum of its digits. 
Return how many groups have the largest size.
 
Example 1:
Input: n = 13
Output: 4
Explanation: There are 9 groups in total, they are grouped according sum of its digits of numbers from 1 to 13:
[1,10], [2,11], [3,12], [4,13], [5], [6], [7], [8], [9]. There are 4 groups with largest size.

Example 2:
Input: n = 2
Output: 2
Explanation: There are 2 groups [1], [2] of size 1.

Example 3:
Input: n = 15
Output: 6

Example 4:
Input: n = 24
Output: 5

 
Constraints:

1 <= n <= 10^4
"""

def count_largest_groups(n: int) -> int:
    # Dictionary to track the groups by sum of digits
    tracker_for_largest = {}
    
    # Variables to track the largest group size and the number of such groups
    largest_size = 0
    num_groups = 0
    
    for num in range(1, n + 1):
        # Calculate the sum of digits of the current number
        curr_sum = sum(int(digit) for digit in str(num))
        
        # Update the tracker dictionary
        if curr_sum not in tracker_for_largest:
            tracker_for_largest[curr_sum] = []
        tracker_for_largest[curr_sum].append(num)
        
        # Check the size of the current group
        group_size = len(tracker_for_largest[curr_sum])
        
        # Update the largest size and number of groups with the largest size
        if group_size == largest_size:
            num_groups += 1
        elif group_size > largest_size:
            num_groups = 1
            largest_size = group_size
    
    return num_groups