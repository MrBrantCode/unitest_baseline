"""
QUESTION:
Write a function `to_uppercase(str)` that converts the input string to all uppercase without using built-in string methods like `.upper()` or any other direct string manipulation libraries. The function should handle special characters and numbers by keeping them unchanged.
"""

def to_uppercase(str):
    result = ""
    for char in str:
        ascii_val = ord(char)
        if ascii_val >= 97 and ascii_val <= 122:  # ASCII values of lowercase letters
            result += chr(ascii_val - 32)  # convert to uppercase
        else:
            result += char  # keep as it is
    return result