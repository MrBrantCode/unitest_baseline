"""
QUESTION:
Create a function `fibonacci(n)` that generates the Nth Fibonacci number using an iterative approach with a time complexity of O(logN) and a space complexity of O(1), where N is a positive integer less than or equal to 10^9.
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