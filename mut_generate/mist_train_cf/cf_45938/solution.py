"""
QUESTION:
Write a function named `fibonacci(n)` that calculates and displays the Fibonacci series up to the 'n-th' position. The function should take a positive integer 'n' as input and return the Fibonacci series. The function should be optimized to handle large values of 'n' (e.g., n>1000) without facing memory- or performance-related issues.
"""

def fibonacci(n):
    a, b = 0, 1
    result = [a]
    for _ in range(n-1):
        a, b = b, a + b
        result.append(a)
    return result