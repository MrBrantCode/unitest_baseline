"""
QUESTION:
Given a binary array arr of size N and an integer target, return the number of non-empty subarrays with a sum equal to target.
Note : A subarray is the contiguous part of the array.
Example 1:
Input:
N = 5
target = 2
arr[ ] = {1, 0, 1, 0, 1}
Output: 4
Explanation: The 4 subarrays are:
{1, 0, 1, _, _}
{1, 0, 1, 0, _}
{_, 0, 1, 0, 1}
{_, _, 1, 0, 1}
 
Example 2:
Input:
N = 5
target = 5
arr[ ] = {1, 1, 0, 1, 1}
Output: 0
Explanation: There is no subarray with sum equal to target.
Your Task:
You don't need to read input or print anything. Your task is to complete the function numberOfSubarrays() which takes the array arr, interger N and an integer target as input and returns the number of subarrays with a sum equal to target.
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
Constraints:
1 ≤ N ≤ 10^{5}
1 ≤ target ≤ N
"""

def numberOfSubarrays(arr, N, target):
    count = 0
    window_sum = 0
    sum_dict = {0: 1}
    
    for num in arr:
        window_sum += num
        if window_sum - target in sum_dict:
            count += sum_dict[window_sum - target]
        if window_sum in sum_dict:
            sum_dict[window_sum] += 1
        else:
            sum_dict[window_sum] = 1
    
    return count