"""
QUESTION:
Create a function named `square_hex_reverse` that takes a list of integers as input and returns a list of strings where each integer is squared, converted to hexadecimal, and then reversed. The hexadecimal representation should not include the '0x' prefix.
"""

def square_hex_reverse(lst):
    result = []
    for num in lst:
        squared = num ** 2
        hexadecimal = hex(squared)[2:]  # Convert to hexadecimal and remove the '0x' prefix
        reversed_hex = hexadecimal[::-1]  # Reverse the hexadecimal string
        result.append(reversed_hex)
    return result