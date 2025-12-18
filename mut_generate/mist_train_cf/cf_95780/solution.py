"""
QUESTION:
Write a function named `binary_to_hexadecimal` that takes a binary string as input and returns its equivalent hexadecimal representation. The input binary string can be negative (indicated by a "-" sign at the start) and can have lengths up to 1 million characters. The function should not use any built-in functions or libraries to perform the conversion, instead implementing the conversion logic from scratch using only basic operations and data structures.
"""

def binary_to_hexadecimal(binary):
    hex_dict = {
        '0000': '0', '0001': '1', '0010': '2', '0011': '3',
        '0100': '4', '0101': '5', '0110': '6', '0111': '7',
        '1000': '8', '1001': '9', '1010': 'A', '1011': 'B',
        '1100': 'C', '1101': 'D', '1110': 'E', '1111': 'F'
    }
    
    hexadecimal = ''
    negative = False
    
    if binary[0] == '-':
        negative = True
        binary = binary[1:]
    
    binary = binary.zfill((len(binary) + 3) // 4 * 4)
    
    for i in range(0, len(binary), 4):
        chunk = binary[i:i+4]
        hexadecimal += hex_dict[chunk]
    
    if negative:
        hexadecimal = '-' + hexadecimal
    
    return hexadecimal