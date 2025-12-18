"""
QUESTION:
Write a function cumulative_cubed_value(n, K) that calculates the cumulative total of the cubed values of all whole numbers within the range of 1 through to and including n, and returns the remainder when this cumulative total is divided by K. The function should have a time complexity of O(1) and be able to handle large inputs where 1 ≤ n, K ≤ 10^9.
"""

def cumulative_cubed_value(n: int, K: int) -> int:
    n = n % K
    return (((n * (n + 1)) // 2) ** 2) % K