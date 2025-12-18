"""
QUESTION:
Develop a function named `fibonacci` that generates the nth Fibonacci number. The function should have a time complexity of O(log n) or better and use constant space. It should handle edge cases such as negative values of n or zero by returning an error message and prevent arithmetic overflow using bitwise operations. The input n should be a non-negative integer.
"""

def fibonacci(n):
    if n <= 0:
        print("Invalid input! n must be a positive integer.")
        return

    a, b = 0, 1
    for _ in range(n - 1):
        a, b = b, (a + b) & ((1 << 64) - 1)

    return a