"""
QUESTION:
Create a function `fibonacci(n)` that returns the `n`th number in the Fibonacci sequence without using recursion, iteration, built-in mathematical functions, loops, or conditional statements. The solution must use only basic arithmetic operations and logical operators, have a time complexity of O(1), and a space complexity of O(1).
"""

def fibonacci(n):
    phi = (1 + 5**0.5) / 2
    return round((phi**n - (-phi)**(-n)) / 5**0.5)