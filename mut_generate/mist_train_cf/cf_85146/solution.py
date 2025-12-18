"""
QUESTION:
Create a function named `hex_key` that takes a string representing a hexadecimal number as input. The function should return the count of hexadecimal characters in the string that correspond to prime numbers (2, 3, 5, 7, 11, 13, etc.) or their hexadecimal representations (B for 11, D for 13). The input string can be empty and is guaranteed to be a valid hexadecimal number with uppercase alphabetic characters.
"""

def hex_key(num):
    count = 0 
    for char in num:
        if char in ['2', '3', '5', '7', 'B', 'D']:
            count += 1 
    return count