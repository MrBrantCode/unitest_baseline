"""
QUESTION:
Given an integer array arr, partition the array into (contiguous) subarrays of length at most k. After partitioning, each subarray has their values changed to become the maximum value of that subarray. Return the largest sum of the given array after partitioning.
Example 1:
Input:
n = 7
k = 3
arr = [1,15,7,9,2,5,10]
Output:
84
Explanation:
arr becomes [15,15,15,9,10,10,10]
Example 2:
Input:
n = 1
k = 1
arr = [1]
Output:
1
Your Task:
You don't have to read input or print anything. Your task is to complete the function Solve() which takes the integer n and array arr and integer k and returns the Largest Sum of the Array after Partitioning.
Expected Time Complexity: O(n^{2})
Expected Space Complexity: O(n)
Constraint:
1 <= n <= 500
0 <= arr[i] <= 10^{9}
1 <= k <= n
"""

def largest_sum_after_partitioning(arr, k):
    import math
    n = len(arr)
    dp = [0] * (n + 1)
    dp[n] = 0
    
    for i in range(n - 1, -1, -1):
        ln, maxi = 0, -math.inf
        ans = -math.inf
        for j in range(i, min(n, i + k)):
            ln += 1
            maxi = max(maxi, arr[j])
            sm = ln * maxi + dp[j + 1]
            ans = max(sm, ans)
        dp[i] = ans
    
    return dp[0]