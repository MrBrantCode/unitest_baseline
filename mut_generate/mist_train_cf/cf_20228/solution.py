"""
QUESTION:
Write a function `decimal_to_hexadecimal` that takes an integer as input and returns its hexadecimal representation as a string using bitwise operations only. The function should not use built-in conversion functions or string formatting. The input integer is non-negative.
"""

def decimal_to_hexadecimal(n):
    hex_map = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
    hex_string = ""
    
    while n > 0:
        # Extract the last 4 bits and convert to hexadecimal
        hex_digit = hex_map[n & 15]
        # Add the hexadecimal digit to the beginning of the hexadecimal string
        hex_string = hex_digit + hex_string
        # Right shift the decimal number by 4 bits
        n = n >> 4
    
    return hex_string if hex_string else '0'