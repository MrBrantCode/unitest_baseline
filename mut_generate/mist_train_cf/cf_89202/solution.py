"""
QUESTION:
Create a function `fibonacci(n)` that calculates the Nth Fibonacci number where N is a positive integer less than or equal to 10^9, with a time complexity of O(logN) and a space complexity of O(1) using an iterative approach.
"""

def fibonacci(n):
    if n <= 0:
        return "Invalid input! n should be a positive integer."

    if n == 1:
        return 0
    elif n == 2:
        return 1

    a, b = 0, 1
    for _ in range(3, n + 1):
        temp = a + b
        a = b
        b = temp

    return b