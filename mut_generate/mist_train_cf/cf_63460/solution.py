"""
QUESTION:
Create a function `remove_special_chars(input_str)` that takes a string as input and returns the string with all special characters removed, while preserving alphanumeric characters and spaces. The function should work with English letters and may not need to support other languages or special scripts.
"""

def remove_special_chars(input_str):
    # use list comprehension to filter out special characters
    output_str = ''.join(char for char in input_str if char.isalnum() or char.isspace())
    return output_str