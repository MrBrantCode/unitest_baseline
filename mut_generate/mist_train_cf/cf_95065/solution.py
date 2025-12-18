"""
QUESTION:
Write a function named `hex_to_bin` that takes a string representing a hexadecimal number and returns a string representing its binary equivalent. The input string will only contain characters from 0-9 and A-F (uppercase) and is a valid hexadecimal number. The function should not use any built-in conversion functions or libraries and should utilize bitwise operators for the conversion.
"""

def hex_to_bin(hex_num):
    # Create a dictionary to map each hexadecimal digit to its binary representation
    hex_to_bin_map = {
        '0': '0000',
        '1': '0001',
        '2': '0010',
        '3': '0011',
        '4': '0100',
        '5': '0101',
        '6': '0110',
        '7': '0111',
        '8': '1000',
        '9': '1001',
        'A': '1010',
        'B': '1011',
        'C': '1100',
        'D': '1101',
        'E': '1110',
        'F': '1111'
    }

    # Convert each hexadecimal digit to its binary representation
    binary_num = ''
    for digit in hex_num:
        binary_num += hex_to_bin_map[digit]

    return binary_num