"""
QUESTION:
Write a function `check_divisible(num1, num2)` that checks whether two numbers are divisible by each other. The function should return `True` if either number is divisible by the other, and `False` otherwise. The function must also handle edge cases, including `ZeroDivisionError` (when the divisor is zero) and `TypeError` (when the inputs are not numbers).
"""

def check_divisible(num1, num2):
    """
    Checks whether two numbers are divisible by each other.
    
    Args:
    num1 (int or float): The first number.
    num2 (int or float): The second number.
    
    Returns:
    bool: True if either number is divisible by the other, False otherwise.
    """
    
    try:
        # Check if either number is divisible by the other
        return num1 % num2 == 0 or num2 % num1 == 0
    except ZeroDivisionError:
        # Handle division by zero error
        return False
    except TypeError:
        # Handle non-numeric input error
        return False