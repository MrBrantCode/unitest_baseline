"""
QUESTION:
Write a function `advanced_hexadecimal_to_binary` that takes a hexadecimal string `x` as input and returns its binary equivalent as a string. The function should not use any built-in or imported functions for conversion. It should handle leading zeroes and accommodate binary numbers up to '1111'. The input `x` is expected to be a valid hexadecimal string, but the function should be able to handle irregular length hexadecimal string inputs.
"""

def advanced_hexadecimal_to_binary(x: str) -> str:
    hex_dict = {"0":"0000","1":"0001", "2":"0010", "3":"0011","4":"0100", "5":"0101", 
                "6":"0110", "7":"0111", "8":"1000", "9":"1001", "A":"1010", 
                "B":"1011", "C":"1100", "D":"1101", "E":"1110", "F":"1111"}

    binary = ''
    for hex_val in x:                 # iterate through each hexadecimal
        binary += hex_dict[hex_val]   # add binary equivalent from dictionary
    # exclude leading zeros 
    binary = binary.lstrip('0')
    if binary == '':
        return '0'
    else:
        return binary