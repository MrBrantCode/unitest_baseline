"""
QUESTION:
Create a function named `convert_case` that takes a string `s` as input and returns a new string with all uppercase letters converted to lowercase and all lowercase letters converted to uppercase. The function should not use any built-in string methods or libraries.
"""

def convert_case(s):
    converted = ""
    for char in s:
        ascii_val = ord(char)
        if 65 <= ascii_val <= 90:  
            converted += chr(ascii_val + 32)
        elif 97 <= ascii_val <= 122:  
            converted += chr(ascii_val - 32)
        else:
            converted += char
    return converted