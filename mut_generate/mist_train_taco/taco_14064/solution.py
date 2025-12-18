"""
QUESTION:
Given an array of positive integers. Find the maximum length of Bitonic subsequence. 
A subsequence of array is called Bitonic if it is first strictly increasing, then strictly decreasing.
 
Example 1:
Input: nums = [1, 2, 5, 3, 2]
Output: 5
Explanation: The sequence {1, 2, 5} is
increasing and the sequence {3, 2} is 
decreasing so merging both we will get 
length 5.
Example 2:
Input: nums = [1, 11, 2, 10, 4, 5, 2, 1]
Output: 6
Explanation: The bitonic sequence 
{1, 2, 10, 4, 2, 1} has length 6.
 
Your Task:
You don't need to read or print anything. Your task is to complete the function LongestBitonicSequence() which takes the array nums[] as input parameter and returns the maximum length of bitonic subsequence.
 
Expected Time Complexity: O(n^{2})
Expected Space Complexity: O(n)
 
Constraints:
1 ≤ length of array ≤ 10^{3}
1 ≤ arr[i] ≤ 10^{6}
"""

def longest_bitonic_sequence(nums):
    n = len(nums)
    
    # Initialize DP arrays for increasing and decreasing subsequences
    dp_inc = [1] * n
    dp_dec = [1] * n
    
    # Compute the length of the longest increasing subsequence ending at each index
    for i in range(n):
        for j in range(i):
            if nums[j] < nums[i] and 1 + dp_inc[j] > dp_inc[i]:
                dp_inc[i] = 1 + dp_inc[j]
    
    # Compute the length of the longest decreasing subsequence starting at each index
    for i in range(n - 1, -1, -1):
        for j in range(n - 1, i, -1):
            if nums[j] < nums[i] and 1 + dp_dec[j] > dp_dec[i]:
                dp_dec[i] = 1 + dp_dec[j]
    
    # Find the maximum length of the bitonic subsequence
    max_length = 0
    for i in range(n):
        max_length = max(max_length, dp_inc[i] + dp_dec[i] - 1)
    
    return max_length