"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given integer `n`, where the factorial of a number is the product of all positive integers from 1 to `n`. The function should have a time complexity of O(n^2) and a space complexity of O(1). The function should return the factorial of `n` if `n` is non-negative, and return `None` if `n` is negative.
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
            for j in range(1, i + 1):
                result += j
        return result