"""
QUESTION:
Write a function named `binary_to_hexadecimal` that takes a binary string as input and returns its equivalent hexadecimal representation as a string. The function should handle negative binary numbers, which are denoted by a "-" sign at the beginning of the string. The function should not use any built-in functions or libraries for the conversion and should be optimized to handle large binary strings efficiently. The input binary string will always be a valid binary representation and will not contain any leading zeros except for negative numbers.
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