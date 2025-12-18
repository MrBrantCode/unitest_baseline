"""
QUESTION:
Create a function `is_power_of_three` to check if a given number `n` is a power of three. If `n` is a power of three, also find the largest power of three that is less than or equal to `n`, and calculate the number of digits in the binary representation of this largest power of three. The function should handle numbers up to 10^12 and have a time complexity of O(log n). If `n` is not a power of three, the function should still find the largest power of three that is less than or equal to `n` and calculate the corresponding binary digits.
"""

import math

def is_power_of_three(n):
    """
    Checks if a given number is a power of three.
    If the number is a power of three, finds the largest power of three that is less than or equal to the number,
    and calculates the number of digits in the binary representation of this largest power of three.
    
    Parameters:
    n (int): The input number to check.
    
    Returns:
    tuple: A boolean indicating whether the number is a power of three, 
           the largest power of three less than or equal to the number, 
           and the number of binary digits in the largest power of three.
    """
    
    # Check if the number is less than or equal to 0
    if n <= 0:
        return False, -1, -1
    
    # Calculate the power of three for the given number
    power = math.log(n, 3)
    
    # Check if the number is a power of three
    is_power = 3 ** round(power) == n
    
    # Calculate the largest power of three less than or equal to the number
    largest_power = 3 ** math.floor(power)
    
    # Calculate the number of binary digits in the largest power of three
    binary_digits = math.floor(math.log2(largest_power)) + 1
    
    return is_power, largest_power, binary_digits