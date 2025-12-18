"""
QUESTION:
Create a function named calculate_factorial that takes an integer age as input and returns its factorial. The function must use a loop to calculate the factorial, not recursion. The input age is obtained from the user through a prompt "Enter your age: ".
"""

def calculate_factorial(age):
    """
    Calculate the factorial of a given number using a loop.

    Args:
    age (int): The number for which the factorial is to be calculated.

    Returns:
    int: The factorial of the given number.
    """
    factorial = 1
    for i in range(1, age + 1):
        factorial *= i
    return factorial