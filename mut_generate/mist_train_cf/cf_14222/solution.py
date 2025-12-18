"""
QUESTION:
Create a function called `divide_numbers` that takes two parameters `a` and `b` and returns their division result. Implement error handling using a try-except block to catch `ZeroDivisionError` that occurs when `b` is zero. Additionally, include another try-except block in the main code to catch any other potential errors, such as `TypeError` due to invalid input type, and print corresponding error messages.
"""

def divide_numbers(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
    except TypeError:
        print("Error: Invalid input type")