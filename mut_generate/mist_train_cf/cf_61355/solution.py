"""
QUESTION:
Write a function named `hex_to_binary` that takes a hexadecimal number as input and returns its equivalent binary numeral system representation as a string. The function should convert each hexadecimal digit into its four-bit binary equivalent and concatenate the results.
"""

def hex_to_binary(hex_num):
    # Define mapping
    mapping = {'0': '0000', '1': '0001', '2': '0010', '3':'0011', 
               '4': '0100', '5': '0101', '6': '0110', '7':'0111',
               '8': '1000', '9': '1001', 'A': '1010', 'B':'1011',
               'C': '1100', 'D': '1101', 'E': '1110', 'F':'1111'}
    
    bin_num = ""
    for digit in hex_num:
        bin_num += mapping[digit]
    return bin_num