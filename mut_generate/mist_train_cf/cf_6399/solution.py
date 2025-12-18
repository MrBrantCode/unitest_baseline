"""
QUESTION:
Create a function named `factorial(n)` that calculates the factorial of a given positive integer `n` where `1 ≤ n ≤ 1000`. The function should not use recursion, have a time complexity of O(n), and a space complexity of O(1).
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result