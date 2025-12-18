"""
QUESTION:
Create a function named `fibonacci` that generates the Fibonacci sequence up to the nth element, where n is a non-negative integer. The function should return a list of integers representing the Fibonacci sequence, starting from 0. The function should handle cases where n is 0, 1, or 2 separately and use iteration for larger values of n.
"""

def fibonacci(n):
    if n <= 0:
        return []
    if n == 1:
        return [0]
    if n == 2:
        return [0, 1]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])

    return fib