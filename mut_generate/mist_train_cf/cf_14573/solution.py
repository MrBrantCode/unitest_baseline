"""
QUESTION:
Create a function `divide_numbers(num1, num2)` that takes two integers as input and returns the result of the division. Both `num1` and `num2` must be positive integers. If either `num1` or `num2` is not a positive integer, or if `num2` is zero, the function should print an error message instead of attempting the division.
"""

def divide_numbers(num1, num2):
    if not (isinstance(num1, int) and isinstance(num2, int)):
        print("Error: Both numbers must be integers.")
    elif num1 <= 0 or num2 <= 0:
        print("Error: Both numbers must be positive integers.")
    elif num2 == 0:
        print("Error: Cannot divide by zero.")
    else:
        return num1 / num2