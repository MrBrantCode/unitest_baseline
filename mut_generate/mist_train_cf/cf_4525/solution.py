"""
QUESTION:
Construct a function `check_number` that takes a number as input and returns a boolean indicating whether the number is divisible by 4, greater than 100, and the sum of its digits is also divisible by 4. The function should handle negative numbers and floating-point numbers.
"""

def check_number(num):
    """
    Checks if a number is divisible by 4, greater than 100, and the sum of its digits is also divisible by 4.
    
    Args:
    num (float): The input number to be checked.
    
    Returns:
    bool: True if the number meets all conditions, False otherwise.
    """
    
    # Check if the number is divisible by 4
    if num % 4 != 0:
        return False
    
    # Check if the number is greater than 100
    if num <= 100:
        return False
    
    # Convert the number to positive if negative
    num = abs(num)
    
    # Check if the sum of its digits is divisible by 4
    digit_sum = sum([int(digit) for digit in str(int(num))])
    if digit_sum % 4 != 0:
        return False
    
    return True