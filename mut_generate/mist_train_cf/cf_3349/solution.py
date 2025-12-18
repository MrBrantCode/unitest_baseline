"""
QUESTION:
Implement a function `replace_with_ascii` that takes a string as input and returns a new string where every letter has been replaced with its corresponding ASCII character code. For lowercase letters, add 32 to the ASCII code before replacing. For uppercase letters, subtract 32 from the ASCII code before replacing. The input string may contain special characters and numbers, which should be left unchanged. Do not use built-in ASCII conversion functions.
"""

def replace_with_ascii(input_string):
    result = ""
    for char in input_string:
        if 97 <= ord(char) <= 122:  
            result += chr(ord(char) + 32)
        elif 65 <= ord(char) <= 90:  
            result += chr(ord(char) - 32)
        else:
            result += char
    return result