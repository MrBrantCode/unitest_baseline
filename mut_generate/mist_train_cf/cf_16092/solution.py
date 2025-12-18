"""
QUESTION:
Create a function `fibonacci(n)` that returns the `n`th number in the Fibonacci sequence. The function should only use basic arithmetic operations and logical operators, without recursion, iteration, or built-in mathematical functions (such as `pow`, `sqrt`, etc.). The time complexity of the solution should be O(1) and the space complexity should be O(1).
"""

def fibonacci(n):
    phi = (1 + (5 ** 0.5)) / 2
    fibonacci_number = int((phi ** n - (-phi) ** (-n)) / (5 ** 0.5))
    return fibonacci_number