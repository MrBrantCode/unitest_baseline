"""
QUESTION:
Create a function `calculate_modulo` that takes three integers as input and returns the remainder of the sum of the first two integers divided by the third. The function should check if all inputs are integers and if the third integer is not zero. If the inputs are not integers or if the third integer is zero, the function should return an error message.
"""

def calculate_modulo(num1, num2, num3):
    if not (isinstance(num1, int) and isinstance(num2, int) and isinstance(num3, int)):
        return "Error: Please provide whole number inputs."
    if num3 == 0:
        return "Error: Division by zero."
    return (num1 + num2) % num3