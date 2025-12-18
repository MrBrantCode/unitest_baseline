"""
QUESTION:
Create a function named `find_remainder` that takes three integers as input. The function should calculate the remainder when the sum of the first two integers is divided by the third integer. If the third integer is zero, the function should return an error message indicating that division by zero is undefined.
"""

def find_remainder(num1, num2, num3):
    """Return the remainder when the sum of the first two numbers is divided by the third number."""
    if num3 == 0:
        return "Invalid operation. Division by zero is undefined"
    return (num1 + num2) % num3