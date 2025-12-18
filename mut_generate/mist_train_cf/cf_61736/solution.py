"""
QUESTION:
Write a function called `fibonacci(n)` that calculates the nth term in the Fibonacci sequence using a for loop. The Fibonacci sequence starts with 0 and 1, and each subsequent term is the sum of the previous two terms. The function should return the nth term. The index is 0-based, meaning `fibonacci(0)` returns the first element and `fibonacci(1)` returns the second element.
"""

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        a, b = b, a + b
    return a