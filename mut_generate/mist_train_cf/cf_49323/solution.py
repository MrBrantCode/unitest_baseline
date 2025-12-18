"""
QUESTION:
Create a function named `is_hex_palindrome` that takes a hexadecimal number as a string as input and returns a boolean indicating whether the hexadecimal number is a palindrome. The input hexadecimal number may contain letters (A-F) and numbers (0-9).
"""

def is_hex_palindrome(hex_num):
    hex_str = str(hex_num)
    return hex_str == hex_str[::-1]