"""
QUESTION:
Write a function `binary_to_hex` that takes a list of binary numbers as strings, converts each binary number into its hexadecimal equivalent, and returns the list of hexadecimal numbers in uppercase. The function should handle lists of up to 1000 binary numbers, with each binary number being up to 16 bits long.
"""

def binary_to_hex(binary_list):
    hex_list = []
    for binary in binary_list:
        hex_value = hex(int(binary, 2))[2:].upper()
        hex_list.append(hex_value)
    return hex_list