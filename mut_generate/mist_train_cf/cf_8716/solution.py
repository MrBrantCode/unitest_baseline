"""
QUESTION:
Write a function named `hex_to_binary` that takes a hexadecimal number as a string and returns its binary representation as a string using bitwise operations. The function should not take any additional arguments other than the hexadecimal number. The input hexadecimal number can contain both digits and letters (A-F).
"""

def hex_to_binary(hex_num):
    binary_num = 0

    for char in hex_num:
        decimal_value = ord(char) - ord('A') + 10 if char.isalpha() else int(char)
        binary_num = (binary_num << 4) | decimal_value

    return bin(binary_num)[2:]