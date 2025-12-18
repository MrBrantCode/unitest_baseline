"""
QUESTION:
Implement a function `fibonacci(n)` to generate the nth element in a Fibonacci series, where n is a positive integer. The function should have a time complexity of O(n) and a space complexity of O(1).
"""

def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        for _ in range(n - 2):
            a, b = b, a + b
        return b