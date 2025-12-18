"""
QUESTION:
Create a function called `divide_numbers` that takes two numbers as arguments and returns their division result. Include a try/except statement in the function to handle a `ZeroDivisionError` that may occur when the second number is zero. Ensure that the function only handles this specific type of exception and not any other possible exceptions.
"""

def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        return result
    
    except ZeroDivisionError:
        return "Error: Division by zero is not allowed."