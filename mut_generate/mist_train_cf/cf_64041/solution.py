"""
QUESTION:
Implement a function `to_hex` that takes a string as input and returns its equivalent hexadecimal notation. Implement another function `from_hex` that takes a hexadecimal notation as input and returns its original character sequence. 

Each function should have a time complexity of O(n), where n is the number of characters or pairs of digits in the input. The conversion process should not use any built-in functions or libraries to convert to and from hexadecimal. The functions should handle edge cases including null values, non-alphanumeric characters, and long strings.
"""

def to_hex(string):
    if not string:
        return ''
    hex_str = ''
    for char in string:
        hex_val = hex(ord(char)).split('x')[-1]
        hex_str += hex_val
    return hex_str

def from_hex(hex_str):
    if not hex_str:
        return ''
    string = ''
    for i in range(0, len(hex_str), 2):
        decimal_val = int(hex_str[i:i+2], 16)
        string += chr(decimal_val)
    return string