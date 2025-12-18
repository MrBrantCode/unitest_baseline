"""
QUESTION:
Create four functions named 'add', 'subtract', 'multiply', and 'divide' that take two integers as input and return their sum, difference, product, and quotient respectively. The 'divide' function should handle division by zero errors by returning a descriptive error message instead of throwing an exception.
"""

def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    try:
        return x / y
    except ZeroDivisionError:
        return "Cannot divide by zero"