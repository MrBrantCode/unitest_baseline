"""
QUESTION:
Write a function named `divide` that takes two numbers `a` and `b` as input and returns their division result. If `b` is zero, the function should return the string "Error: Division by zero". Write a unit test for this function to ensure it handles both division by non-zero and zero correctly.
"""

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b