"""
QUESTION:
Implement a function named `factorial` that takes an integer `n` as input and returns the factorial of `n` with a time complexity of O(n^2) and a space complexity of O(1). The function should handle cases where `n` is less than 0 and return `None`, and where `n` is 0 and return 1.
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