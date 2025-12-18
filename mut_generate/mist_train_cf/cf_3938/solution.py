"""
QUESTION:
Implement the `fibonacci` function to calculate the n-th Fibonacci number, where n is a non-negative integer. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def fibonacci(n):
    if n <= 1:
        return n

    a, b = 0, 1
    i = 2

    while i <= n:
        a, b = b, a + b
        i += 1

    return b