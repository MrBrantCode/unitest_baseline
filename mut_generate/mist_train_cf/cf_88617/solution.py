"""
QUESTION:
Create a function `is_power_of_three(n)` that checks if a given integer `n` is a power of three, and if so, finds the largest power of three that is less than or equal to `n`. Additionally, the function should output the number of digits in the binary representation of the largest power of three. The function should handle numbers up to 10^12 and have a time complexity of O(log n).
"""

import math

def is_power_of_three(n):
    if n <= 0:
        return False, -1, -1
    
    power = math.log(n, 3)
    largest_power = 3 ** math.floor(power)
    
    if 3 ** round(power) == n:
        binary_digits = math.floor(math.log2(largest_power)) + 1
        return True, largest_power, binary_digits
    else:
        binary_digits = math.floor(math.log2(largest_power)) + 1
        return False, largest_power, binary_digits