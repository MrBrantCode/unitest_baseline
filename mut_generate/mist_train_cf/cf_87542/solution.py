"""
QUESTION:
Write a function called `find_max` that takes five numbers as arguments and returns the maximum of these numbers without using the built-in max() function and any conditional statements. The function should work for any set of five numbers.
"""

def find_max(num1, num2, num3, num4, num5):
    """
    This function takes five numbers as arguments and returns the maximum of these numbers.
    
    Parameters:
    num1 (int): The first number.
    num2 (int): The second number.
    num3 (int): The third number.
    num4 (int): The fourth number.
    num5 (int): The fifth number.
    
    Returns:
    int: The maximum of the five numbers.
    """
    numbers = [num1, num2, num3, num4, num5]
    numbers.sort()
    return numbers[-1]