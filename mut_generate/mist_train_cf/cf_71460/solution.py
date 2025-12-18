"""
QUESTION:
Create a function called binaryToNumpyArray() that takes an integer as input, converts it to its binary form, and then converts the binary string into a NumPy array where each digit is an individual element of the array. The function should return the resulting NumPy array. Use the "random" and "numpy" packages.
"""

import numpy as np

def binaryToNumpyArray(number):
    binary = format(number, 'b')    # Convert number to binary
    bin_list = list(binary)         # Convert binary string to list
    return np.array(list(map(int, bin_list)))