"""
QUESTION:
Create a function `decimal_to_binary` that takes an integer `number` as input and returns its binary representation as a string using a recursive approach. The function should be able to handle integers up to 10^9. Additionally, create a function `count_ones` that takes a binary string as input and returns the number of '1's in the string. Use these functions to convert the given number to binary and count the number of '1's in its binary representation.
"""

def decimal_to_binary(number):
    if number == 0:
        return ""
    else:
        return decimal_to_binary(number // 2) + str(number % 2)

def count_ones(binary):
    return binary.count('1')