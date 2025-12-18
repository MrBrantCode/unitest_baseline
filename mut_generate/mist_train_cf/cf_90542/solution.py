"""
QUESTION:
Write a function `hex_to_binary(hex_num)` that takes a string representing a hexadecimal number as input and returns its binary form as a string using bitwise operations only. The input hexadecimal number may contain both letters and numbers, and the output binary string should not have the '0b' prefix.
"""

def hex_to_binary(hex_num):
    binary_num = 0

    for char in hex_num:
        decimal_value = ord(char) - ord('A') + 10 if char.isalpha() else int(char)
        binary_num = (binary_num << 4) | decimal_value

    return bin(binary_num)[2:]