"""
QUESTION:
Create a function called `hex_to_bin` that takes a string of hexadecimal digits as input and returns its binary representation as a string. The function should handle both uppercase and lowercase hexadecimal digits, and return an error message if the input contains any invalid characters. Do not use any built-in or library functions for the conversion.
"""

def hex_to_bin(hex_num):
    hex_to_bin_dict = {'0':'0000', 
                       '1':'0001',
                       '2':'0010', 
                       '3':'0011',
                       '4':'0100', 
                       '5':'0101', 
                       '6':'0110', 
                       '7':'0111', 
                       '8':'1000', 
                       '9':'1001', 
                       'A':'1010', 
                       'B':'1011',
                       'C':'1100', 
                       'D':'1101', 
                       'E':'1110',
                       'F':'1111',
                       'a':'1010', 
                       'b':'1011', 
                       'c':'1100', 
                       'd':'1101',
                       'e':'1110', 
                       'f':'1111'}

    bin_num = ""
    
    for hex_digit in hex_num:
        if hex_digit in hex_to_bin_dict:
            bin_num += hex_to_bin_dict[hex_digit]
        else:
            return "Error: Invalid hexadecimal number"
    
    return bin_num