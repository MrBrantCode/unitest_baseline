"""
QUESTION:
You are given a non-negative integer n, find the total number of full staircase rows that can be formed with n coins, where every k-th row must have exactly k coins and every 3rd row must have an extra coin. The input integer n is within the range of a 32-bit signed integer. Write a function `arrangeCoins(n)` to return the maximum number of full staircase rows that can be formed.
"""

def arrangeCoins(n):
    left, right = 0, n
    while left < right:
        mid = (left + right + 1) // 2
        if mid * (mid + 1) // 2 + mid // 3 <= n:
            left = mid
        else:
            right = mid - 1
    if left * (left + 1) // 2 + left // 3 > n:
        return left - 1
    else:
        return left