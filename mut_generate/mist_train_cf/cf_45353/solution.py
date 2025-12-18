"""
QUESTION:
Implement a Python program with four separate functions (`add`, `subtract`, `multiply`, `divide`) that take two parameters (`x` and `y`) and perform the corresponding arithmetic operation. The functions should handle exceptions for invalid inputs (non-numeric) and division by zero, returning error messages for these cases.
"""

def add(x, y):
    try:
        return x + y
    except TypeError:
        return "Invalid inputs. Please make sure both inputs are numbers."

def subtract(x, y):
    try:
        return x - y
    except TypeError:
        return "Invalid inputs. Please make sure both inputs are numbers."

def multiply(x, y):
    try:
        return x * y
    except TypeError:
        return "Invalid inputs. Please make sure both inputs are numbers."

def divide(x, y):
    try:
        return x / y
    except TypeError:
        return "Invalid inputs. Please make sure both inputs are numbers."
    except ZeroDivisionError:
        return "Can't divide by zero."