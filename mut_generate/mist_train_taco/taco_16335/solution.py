"""
QUESTION:
Given an array arr[] of positive integers of size N and an integer target, replace each element in the array such that the difference between adjacent elements in the array is less than or equal to a given target. We need to minimize the adjustment cost, that is the sum of differences between new and old values. We basically need to minimize ∑|A[i]  A_{new}[i]| where 0 <= i <= n-1, n is size of A[] and A_{new}[] is the array with adjacent difference less than or equal to target.Assume all elements of the array is less than constant M = 100.
 
Example 1:
Input: N = 4, target = 1
arr[] = { 1, 3, 0, 3 }
Output: 3
Explanation: One of the possible 
solutions is [2, 3, 2, 3].
Example 2:
Input: N = 4, target = 1
arr[] = {2, 3, 2, 3}
Output: 0
Explanation: All adjacent elements 
in the input array are already less 
than equal to given target.
Your Task:
This is a function problem. You don't need to take any input, as it is already accomplished by the driver code. You just need to complete the function minAdjustmentCost() that takes array arr[] , integer n, and integer target as parameters and returns the minimum adjustment cost.
 
Expected Time Complexity: O(N).
Expected Auxiliary Space: O(1).
 
Constraints:
1 ≤ N ≤ 10^{2}
"""

def min_adjustment_cost(arr, target):
    n = len(arr)
    M = max(arr)
    dp = [[0 for _ in range(M + 1)] for _ in range(n)]
    
    # Initialize the first row of dp array
    for j in range(M + 1):
        dp[0][j] = abs(j - arr[0])
    
    # Fill the dp array
    for i in range(1, n):
        for j in range(M + 1):
            dp[i][j] = float('inf')
            for k in range(max(j - target, 0), min(M, j + target) + 1):
                dp[i][j] = min(dp[i][j], dp[i - 1][k] + abs(arr[i] - j))
    
    # Find the minimum adjustment cost
    res = float('inf')
    for j in range(M + 1):
        res = min(res, dp[n - 1][j])
    
    return res