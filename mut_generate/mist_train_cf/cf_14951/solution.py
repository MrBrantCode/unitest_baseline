"""
QUESTION:
Write a function named `convert_binary_to_hex` that takes a binary number as input and returns its equivalent hexadecimal representation as a string. The hexadecimal output should be in uppercase. The function should be able to handle binary numbers of any length.
"""

def convert_binary_to_hex(binary_num):
    decimal_num = int(binary_num, 2)
    hex_num = hex(decimal_num)[2:]  # [2:] to remove '0x' from the hexadecimal string
    return hex_num.upper()