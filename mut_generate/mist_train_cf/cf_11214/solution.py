"""
QUESTION:
Write a function named `hex_to_binary` that converts a given hexadecimal number to binary format using bitwise operators without using any built-in conversion functions. The input is a string representing a hexadecimal number and the output should be a string of the binary representation.
"""

def hex_to_binary(hex_str):
    hex_to_bin = {
        '0': '0000', '1': '0001', '2': '0010', '3': '0011',
        '4': '0100', '5': '0101', '6': '0110', '7': '0111',
        '8': '1000', '9': '1001', 'A': '1010', 'B': '1011',
        'C': '1100', 'D': '1101', 'E': '1110', 'F': '1111'
    }
    
    binary = ''
    for char in hex_str:
        binary += hex_to_bin[char.upper()]
    return binary