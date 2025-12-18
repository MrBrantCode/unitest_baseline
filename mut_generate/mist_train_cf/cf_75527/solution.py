"""
QUESTION:
Create a function named `factorial(num)` that calculates the factorial of a given non-negative integer `num`. The function should return the product of all positive integers less than or equal to `num` if `num` is non-negative, and an error message if `num` is negative.
"""

def factorial(num):
    """
    This function takes a non-negative integer and calculates its factorial.
    Factorial of a number is the product of all positive integers less than or equal to it.
    """
    if num < 0: 
        return "Invalid input! Please enter a non-negative integer."
    elif num == 0 or num == 1: 
        return 1
    else: 
        return num * factorial(num - 1)