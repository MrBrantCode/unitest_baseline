"""
QUESTION:
Create a function named `divide` that takes two parameters, `a` and `b`, and returns their division result. The function should handle the case where `b` is zero to prevent a division by zero error.
"""

def divide(a, b):
    try: 
        return a/b
    except ZeroDivisionError:
        print("Division by zero is undefined")