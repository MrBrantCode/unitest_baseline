"""
QUESTION:
Create a function `sum_multiple_of_five(num1, num2)` that takes two arguments and returns a boolean value indicating if their sum is a multiple of 5. If either of the inputs cannot be converted to a number, the function should return an error message.
"""

def sum_multiple_of_five(num1, num2):
    try:
        num1 = float(num1)
        num2 = float(num2)
        return (num1 + num2) % 5 == 0
    except ValueError:
        return "Error: Non-numeric inputs"