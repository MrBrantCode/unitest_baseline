"""
QUESTION:
Define a function named `calculate_product` that takes three integers `num1`, `num2`, and `num3` as input and returns their product if all three numbers are unique. If any two numbers are equal, the function should return an error message.
"""

def calculate_product(num1, num2, num3):
    if num1 == num2 or num1 == num3 or num2 == num3:
        return "Error: All three numbers must be unique."
    else:
        return num1 * num2 * num3