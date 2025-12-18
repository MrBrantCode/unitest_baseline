"""
QUESTION:
Create a function `divide(x, y)` that takes two numbers as input and returns their division result. The function must handle the case where `y` is zero and print "Error: Division by zero is not allowed." instead of stopping execution. Implement the function using exception handling and ensure it only catches the specific exception type related to division by zero.
"""

def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    else:
        return result