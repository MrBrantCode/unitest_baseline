"""
QUESTION:
Design a recursive function named `fibonacci` that calculates the n'th Fibonacci number. The function should have a time complexity of O(2^n) and a space complexity of O(n). It should handle negative input values by returning an error message.
"""

def fibonacci(n):
    if n < 0:
        return "Error: Fibonacci sequence is not defined for negative numbers."
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)