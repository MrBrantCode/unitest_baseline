"""
QUESTION:
Write a function `factorial(n)` that calculates the product of all positive odd integers less than or equal to `n`. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def factorial(n):
    result = 1
    for i in range(n, 0, -2):
        if i % 2 != 0:
            result *= i
    return result