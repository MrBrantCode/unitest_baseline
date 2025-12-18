"""
QUESTION:
Create a function called `highest_common_factor` that takes two parameters, `num1` and `num2`, and returns their highest common factor using a recursive method without using built-in math functions. The function should only accept non-zero integers as inputs and return an error message for any invalid inputs.
"""

def highest_common_factor(num1, num2):
    """
    This function calculates the highest common factor of two integers using recursion.
    
    Args:
        num1 (int): The first integer.
        num2 (int): The second integer.
    
    Returns:
        int: The highest common factor of num1 and num2.
        str: An error message if either input is not a non-zero integer.
    """
    
    # Check if both numbers are integers and non-zero
    if not isinstance(num1, int) or not isinstance(num2, int) or num1 == 0 or num2 == 0:
        return "Error: Both the inputs have to be non-zero integers!"
    else:
        if num1 > num2:
            if num1 % num2 == 0:
                return num2
            else:
                return highest_common_factor(num2, num1 % num2)
        else:
            if num2 % num1 == 0:
                return num1
            else:
                return highest_common_factor(num1, num2 % num1)