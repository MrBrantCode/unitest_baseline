"""
QUESTION:
Write a function called `divide` that takes two parameters `a` and `b` and returns their division result. The function should handle division by zero by returning the string "Error: Division by zero".
"""

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b