"""
QUESTION:
Write a function `divide_with_error_handling` that takes two arguments `a` and `b` and returns their division result. The function should handle two types of exceptions: `ZeroDivisionError` and `TypeError`. If a `ZeroDivisionError` occurs, it should print "Error: Division by zero" and return `None`. If a `TypeError` occurs, it should print "Error: Invalid input type" and return `None`. If no exceptions occur, it should return the division result.

The function should also intentionally include a logical error that will cause the program to produce an incorrect output or fail to execute. The candidates should identify and fix the error to achieve the desired result. 

Note that the division operation should be performed regardless of whether the inputs are integers or floating-point numbers.
"""

def divide_with_error_handling(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Division by zero")
        return None
    except TypeError:
        print("Error: Invalid input type")
        return None