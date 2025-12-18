"""
QUESTION:
Write a function named `fibonacci` that calculates the n-th Fibonacci number for a given non-negative integer n. The function should handle negative values of n by returning an error message. The function must have a time complexity of O(n) and a space complexity of O(1), and be able to handle large values of n (e.g. n = 10^6) efficiently.
"""

def fibonacci(n):
    if n < 0:
        return "Invalid input: n must be a non-negative integer."
    if n == 0:
        return 0
    if n == 1:
        return 1
    
    a = 0
    b = 1
    for _ in range(2, abs(n) + 1):
        a, b = b, a + b
    
    return b if n > 0 else -b