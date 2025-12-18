"""
QUESTION:
Implement a function `fibonacci(n)` that returns the nth Fibonacci number. The function should handle negative input values by printing an error message and returning. The solution should have a time complexity of O(n) and space complexity of O(1).
"""

def fibonacci(n):
    if n < 0:
        print("Error: Input value should be non-negative.")
        return

    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n+1):
            a, b = b, a + b
        return b