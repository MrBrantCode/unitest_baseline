"""
QUESTION:
Write a function `check_divisibility` that takes two integers as input. The integers must be between 0 and 100, inclusive. The function should return "Divisible" if the first integer is divisible by the second integer without a remainder, and "Not Divisible" otherwise. If the inputs are not valid integers within the specified range, return "Invalid input".
"""

def check_divisibility(variable1, variable2):
    """
    Checks if variable1 is divisible by variable2 without a remainder.
    
    Args:
        variable1 (int): The dividend. Must be between 0 and 100, inclusive.
        variable2 (int): The divisor. Must be between 0 and 100, inclusive.
    
    Returns:
        str: "Divisible" if variable1 is divisible by variable2, "Not Divisible" otherwise.
             "Invalid input" if variable1 or variable2 is not a valid integer.
    """
    if isinstance(variable1, int) and isinstance(variable2, int) and 0 <= variable1 <= 100 and 0 < variable2 <= 100:
        if variable1 % variable2 == 0:
            return "Divisible"
        else:
            return "Not Divisible"
    else:
        return "Invalid input"