"""
QUESTION:
Given a positive integer n, index, and maxSum, construct an array nums of length n that satisfies the following conditions: 
- The sum of all elements of nums does not exceed maxSum.
- The absolute difference between adjacent elements in nums does not exceed 1.
- The array is a palindrome (i.e., nums[i] equals nums[n-i-1] for all i).
- The value at the given index is maximized.

Write a function maxValue that returns the maximum possible value at the given index under these constraints. The function should take three parameters: n (1 <= n <= maxSum <= 10^9), index (0 <= index < n), and maxSum.
"""

def maxValue(n: int, index: int, maxSum: int) -> int:
    maxSum -= n
    l, r = 0, maxSum
    while l < r:
        m = (l + r + 1) // 2
        if m > maxSum - min(m, index) * (min(m, index) + 1) // 2 - min(m, n - index - 1) * (min(m, n - index - 1) + 1) // 2: 
            r = m - 1
        else: 
            l = m
    return l + 1