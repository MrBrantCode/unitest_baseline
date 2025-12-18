"""
QUESTION:
Create a function called `sum_between_numbers` that takes two integers as input and returns the sum of all the numbers between them (inclusive). The input integers can be in any order.
"""

def sum_between_numbers(num1, num2):
    """
    Calculate the sum of all the numbers between num1 and num2 (inclusive).
    
    Args:
    num1 (int): The first integer.
    num2 (int): The second integer.
    
    Returns:
    int: The sum of all the numbers between num1 and num2 (inclusive).
    """
    # Swap num1 and num2 if num1 is greater than num2
    if num1 > num2:
        num1, num2 = num2, num1
    
    # Calculate the sum of all numbers between num1 and num2 (inclusive)
    return sum(range(num1, num2 + 1))