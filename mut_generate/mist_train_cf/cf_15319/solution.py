"""
QUESTION:
Create a function `square_hex_reverse` that takes a list of integers as input, squares each integer, converts it to hexadecimal, reverses the hexadecimal string, and returns a list of the resulting strings. The hexadecimal conversion should not include the '0x' prefix.
"""

def square_hex_reverse(lst):
    result = []
    for num in lst:
        squared = num ** 2
        hexadecimal = hex(squared)[2:]  # Convert to hexadecimal and remove the '0x' prefix
        reversed_hex = hexadecimal[::-1]  # Reverse the hexadecimal string
        result.append(reversed_hex)
    return result