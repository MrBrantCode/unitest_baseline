"""
QUESTION:
Write a function `checkBinaryPrime(bin_num)` that takes a string `bin_num` representing a binary number as input and returns a string indicating whether the binary number corresponds to a prime number in its decimal equivalent. The function should return 'Not a valid binary number.' if the input is not a valid binary number.
"""

import re
from math import sqrt

def checkBinaryPrime(bin_num):
    # Regex expression to match binary numbers
    pattern = re.compile('^[01]+$')
    if not pattern.match(bin_num):
        return 'Not a valid binary number.'
    
    # Convert binary to decimal
    decimal = int(bin_num, 2) 
    
    # Return False if number is less than 2
    if (decimal < 2): 
        return f'The decimal equivalent of {bin_num} is {decimal}, which is not a prime number.'
    
    # Check if number is divisible upto it's square root
    for i in range(2, int(sqrt(decimal)) + 1):
        if decimal % i == 0:
            return f'The decimal equivalent of {bin_num} is {decimal}, which is not a prime number.'
    
    return f'The decimal equivalent of {bin_num} is {decimal}, which is a prime number.'