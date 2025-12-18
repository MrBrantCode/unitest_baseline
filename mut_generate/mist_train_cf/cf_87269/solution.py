"""
QUESTION:
Write a function called `fibonacci` that calculates the n-th Fibonacci number. The function should return an error message if n is a negative integer. The function should have a time complexity of O(n) and space complexity of O(1), and be able to handle large values of n efficiently.
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