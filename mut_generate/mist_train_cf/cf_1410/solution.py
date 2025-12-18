"""
QUESTION:
Write a function named `factorial` that calculates the product of all positive odd integers less than or equal to a given number `n`. The solution should have a time complexity of O(n) and a space complexity of O(1).
"""

def factorial(n):
    result = 1
    for i in range(n, 0, -2):
        result *= i
    return result