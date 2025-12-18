"""
QUESTION:
Write a function named `factorial(n)` to calculate the factorial of a non-negative integer `n` iteratively. The function should return `None` for negative inputs, 1 for 0, and the calculated factorial for positive integers. The implementation should have a time complexity of O(n), where n is the input number, and should not use the built-in `math.factorial()` function.
"""

def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        result = 1
        for i in range(1, n + 1):
            result *= i
        return result