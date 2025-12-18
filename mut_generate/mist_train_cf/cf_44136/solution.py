"""
QUESTION:
Construct a recursive function named `process_str` that accepts a string `data` and an optional integer `index` with a default value of 0. The function should iterate through each character in the string, swapping the case of alphabetic characters without using built-in lower or upper case functions, and return the resulting string.
"""

def process_str(data, index=0):
    if index == len(data):
        return ""
    else:
        char = data[index]
        ascii_val = ord(char)
        if 65 <= ascii_val <= 90:  # ASCII value of uppercase letters (A-Z)
            new_char = chr(ascii_val + 32)  # Convert to lowercase
        elif 97 <= ascii_val <= 122:  # ASCII value of lowercase letters (a-z)
            new_char = chr(ascii_val - 32)  # Convert to uppercase
        else:
            new_char = char  
        return new_char + process_str(data, index + 1)