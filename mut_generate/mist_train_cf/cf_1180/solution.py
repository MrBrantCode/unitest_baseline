"""
QUESTION:
Write a function named `fibonacci` that calculates the nth Fibonacci number using recursion. The function should have a time complexity of O(n) and space complexity of O(n), and it should handle inputs up to 10^5. Ensure the function correctly handles edge cases and avoids infinite recursion.
"""

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2)