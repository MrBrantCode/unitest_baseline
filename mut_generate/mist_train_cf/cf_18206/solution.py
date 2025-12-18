"""
QUESTION:
Write a function `calculate_factorial()` that takes an integer input from the user, calculates its factorial, and displays both the factorial and the sum of all its digits. The function should validate the input to ensure it is a positive integer, handling negative integers, zero, and non-integer inputs by prompting the user to enter a valid input.
"""

def calculate_factorial(num):
    """
    Calculates the factorial of a given number and the sum of its digits.
    
    Args:
        num (int): The input number.
    
    Returns:
        tuple: A tuple containing the factorial and the sum of its digits.
    """
    
    # Initialize factorial
    factorial = 1
    
    # Calculate factorial
    for i in range(1, num + 1):
        factorial *= i

    # Calculate sum of digits in factorial
    sum_of_digits = sum(int(digit) for digit in str(factorial))
    
    return factorial, sum_of_digits