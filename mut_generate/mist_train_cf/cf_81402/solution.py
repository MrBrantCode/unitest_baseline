"""
QUESTION:
Write a function `fast_function(n)` that calculates the sum of the squares of the first n natural numbers with improved performance compared to the existing solution that uses a loop. The function should take an integer `n` as input and return the calculated sum. The improved solution should utilize a mathematical formula to achieve better performance, and it should be able to handle large values of `n` without significant performance degradation.
"""

def optimized_function(n):
    return n * (n + 1) * (2 * n + 1) // 6