"""
QUESTION:
Create a function called `compare_numbers` that takes two parameters `num1` and `num2`. The function should return a string indicating the comparison result. If `num1` is smaller than `num2`, it should return "num1 is smaller than num2". If `num1` is greater than `num2`, it should return "num1 is greater than num2". If `num1` is equal to `num2`, it should return "num1 is equal to num2". Use a ternary operator to achieve this.
"""

def compare_numbers(num1, num2):
    """
    This function compares two numbers and returns a string indicating the comparison result.
    
    Parameters:
    num1 (int): The first number to compare.
    num2 (int): The second number to compare.
    
    Returns:
    str: A string indicating the comparison result.
    """
    return "num1 is smaller than num2" if num1 < num2 else "num1 is greater than num2" if num1 > num2 else "num1 is equal to num2"