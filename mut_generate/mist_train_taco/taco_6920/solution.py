"""
QUESTION:
You are given an array arr[] of size n. Find the total count of sub-arrays having their sum equal to 0.
Example 1:
Input:
n = 6
arr[] = {0,0,5,5,0,0}
Output: 6
Explanation: The 6 subarrays are 
[0], [0], [0], [0], [0,0], and [0,0].
Example 2:
Input:
n = 10
arr[] = {6,-1,-3,4,-2,2,4,6,-12,-7}
Output: 4
Explanation: The 4 subarrays are [-1 -3 4]
[-2 2], [2 4 6 -12], and [-1 -3 4 -2 2]
Your Task:
You don't need to read input or print anything. Complete the function findSubarray() that takes the array arr and its size n as input parameters and returns the total number of sub-arrays with 0 sum. 
 
Expected Time Complexity: O(n*log(n))
Expected Auxilliary Space: O(n)
 
Constraints:    
1 <= n <= 10^6
-10^9 <= arr[ i ] <= 10^9
"""

def count_zero_sum_subarrays(arr, n):
    # Dictionary to store the frequency of prefix sums
    prefix_sum_count = {}
    count = 0
    current_sum = 0
    
    for i in range(n):
        current_sum += arr[i]
        
        # If the current sum is 0, we found a new subarray starting from the beginning
        if current_sum == 0:
            count += 1
        
        # If the current sum has been seen before, it means there are subarrays with sum 0
        if current_sum in prefix_sum_count:
            count += prefix_sum_count[current_sum]
            prefix_sum_count[current_sum] += 1
        else:
            prefix_sum_count[current_sum] = 1
    
    return count