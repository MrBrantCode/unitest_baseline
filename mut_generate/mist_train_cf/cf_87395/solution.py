"""
QUESTION:
Write a function `fibonacci` that calculates the nth Fibonacci number using an efficient approach. The Fibonacci sequence is defined as: F(0) = 0, F(1) = 1, and F(n) = F(n-1) + F(n-2) for n > 1. The function should have a time complexity of O(n) for large values of n.
"""

def fibonacci(num, memo={}):
    if num in memo:
        return memo[num]
    if num <= 1:
        return num
    memo[num] = fibonacci(num-1, memo) + fibonacci(num-2, memo)
    return memo[num]