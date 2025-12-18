"""
QUESTION:
Write a recursive function called `fibonacci` that calculates the nth Fibonacci number in a sequence where the first two numbers are 0 and 1, and each subsequent number is the sum of the two preceding ones. The function should have a time complexity of O(n) and a space complexity of O(n), and it should accept a non-negative integer `n` as input.
"""

def fibonacci(n):
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Recursive call
    return fibonacci(n-1) + fibonacci(n-2)