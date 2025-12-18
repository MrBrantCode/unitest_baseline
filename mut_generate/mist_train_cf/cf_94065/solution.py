"""
QUESTION:
Create a function `fibonacci(n)` that calculates the `n`th Fibonacci number without using recursion, iteration, or built-in mathematical functions such as `pow`, `sqrt`, etc. The function should use only basic arithmetic operations and logical operators, and its time complexity should be O(1) and space complexity O(1).
"""

def fibonacci(n):
    phi = (1 + (5 ** 0.5)) / 2
    fibonacci_number = int((phi ** n - (1-phi) ** n) / (5 ** 0.5))
    return fibonacci_number