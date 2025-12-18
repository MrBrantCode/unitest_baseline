"""
QUESTION:
Create a function named `calculateSum` that takes two positive integer parameters. The function should only work with numbers between 1 and 100 (inclusive). If either of the input numbers is outside this range, return the error message "Error: Numbers should be between 1 and 100 (inclusive)". Additionally, if the sum of the two numbers is divisible by 3, return the error message "Error: The sum is divisible by 3". Otherwise, return the sum of the two numbers.
"""

def calculate_sum(num1: int, num2: int) -> int or str:
    """
    This function calculates the sum of two positive integers between 1 and 100 (inclusive).
    
    Args:
        num1 (int): The first positive integer.
        num2 (int): The second positive integer.
    
    Returns:
        int or str: The sum of the two numbers if it's not divisible by 3, otherwise an error message.
    """

    if not (1 <= num1 <= 100) or not (1 <= num2 <= 100):
        return "Error: Numbers should be between 1 and 100 (inclusive)."
    elif (num1 + num2) % 3 == 0:
        return "Error: The sum is divisible by 3."
    else:
        return num1 + num2