"""
QUESTION:
Write a function named `factorial` that calculates the factorial of a given number `n` using an iterative approach. The function should have a time complexity of O(n) and a space complexity of O(1), not including the space needed for the output.
"""

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result