"""
QUESTION:
Create a function called `calculate_product` that takes three numbers as input and returns their product. The function must check that all three numbers are unique, and if any two numbers are equal, it returns an error message instead.
"""

def calculate_product(num1, num2, num3):
    if num1 == num2 or num1 == num3 or num2 == num3:
        return "Error: All three numbers must be unique."
    else:
        return num1 * num2 * num3