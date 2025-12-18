"""
QUESTION:
Create a function `compare_numbers(num1, num2)` that takes two integers as input and returns a string describing their relationship. The function should return "num1 is smaller than num2" if num1 is less than num2, "num1 is greater than or equal to num2" if num1 is greater than or equal to num2, and "num1 is equal to num2" if num1 is equal to num2. Use ternary operators to implement the logic.
"""

def compare_numbers(num1, num2):
    """
    This function compares two integers and returns a string describing their relationship.
    
    Args:
        num1 (int): The first number for comparison.
        num2 (int): The second number for comparison.
    
    Returns:
        str: A string describing the relationship between num1 and num2.
    """
    return "num1 is smaller than num2" if num1 < num2 else "num1 is greater than num2" if num1 > num2 else "num1 is equal to num2"