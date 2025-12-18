"""
QUESTION:
Implement a function `hex_to_oct(nums)` that takes a dynamic-sized array of strings representing hexadecimal numbers and returns their corresponding octal representations. The function should validate the input hexadecimal numbers and return an error message for the first invalid input encountered, specifying the invalid number. Optimize the function for performance to handle input arrays of up to 1000 elements.
"""

import re

def hex_to_oct(nums):
    result = []
    for num in nums:
        if re.fullmatch(r"([0-9a-fA-F]*)", num) is not None:
            dec = int(num, 16)
            octal = oct(dec)[2:]
            result.append(octal)
        else:
            return "Error: {} is not a valid hexadecimal number.".format(num)
    return result