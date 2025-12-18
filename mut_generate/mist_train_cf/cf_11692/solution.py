"""
QUESTION:
Write a function called `safe_division` that takes two integers as input and returns their division result. The function should include a try-catch block to handle the case when the divisor is zero, in which case it should print "Error: Division by zero is not allowed" and return None.
"""

def safe_division(dividend, divisor):
    try:
        result = dividend / divisor
        return result
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed")
        return None