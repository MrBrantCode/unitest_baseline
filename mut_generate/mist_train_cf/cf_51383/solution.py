"""
QUESTION:
Write a function named `hex_to_dec` that takes a hexadecimal string of arbitrary length as input. The function should determine whether the number represented by the hexadecimal string is odd or even and return a string ('ODD' or 'EVEN') along with the decimal value of the last hexadecimal digit. The function must not use any built-in hexadecimal conversion functions.
"""

def hex_to_dec(hex_string):
    hex_to_dec_map = {
        '0': 0, '1': 1, '2': 2, '3': 3, '4': 4,
        '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
        'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
        'a': 10, 'b': 11, 'c': 12, 'd': 13, 'e': 14, 'f': 15,
    }
    
    last_hex_digit = hex_string[-1]
    last_dec_digit = hex_to_dec_map[last_hex_digit]

    odd_or_even = 'EVEN' if last_dec_digit % 2 == 0 else 'ODD'
    
    return odd_or_even, last_dec_digit