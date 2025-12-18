"""
QUESTION:
Create a function named `divide_and_return_integer` that takes two integers `dividend` and `divisor` as input, and returns the quotient as an integer. The function should handle division by zero error, either by returning a specific value or printing an error message.
"""

def divide_and_return_integer(dividend, divisor):
    try:
        quotient = dividend / divisor
        return int(quotient)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed!")
        return None