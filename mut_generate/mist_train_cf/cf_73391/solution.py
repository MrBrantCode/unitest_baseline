"""
QUESTION:
Write a function named `Binary_Analysis` that takes a binary number as input and returns a tuple containing the following information: 
- The number of zeroes in the binary number.
- The number of ones in the binary number.
- The number of groups of consecutive zeroes in the binary number.
- The number of groups of consecutive ones in the binary number.

The input binary number is a string of '0's and '1's. The function should not take any other parameters besides the binary number.
"""

import re

def Binary_Analysis(binary):
    # Convert binary to string
    binary_str = str(binary)
    number_of_zeros =  binary_str.count('0')
    number_of_ones = binary_str.count('1')

    p = re.compile('1+')
    number_of_consecutive_ones = len(p.findall(binary_str))

    p = re.compile('0+')
    number_of_consecutive_zeroes = len(p.findall(binary_str))

    return(number_of_zeros,number_of_ones,number_of_consecutive_zeroes,number_of_consecutive_ones)