"""
QUESTION:
Write a function `upper_case(s)` that takes a string `s` as input and returns the string with all lowercase letters converted to uppercase, without using built-in string methods or functions. Non-alphabetic characters, including digits, should remain unchanged.
"""

def upper_case(s):
    upper_s = ""
    for char in s:
        ascii_val = ord(char)
        if 97 <= ascii_val <= 122: # ASCII range for small letter a-z
            upper_s += chr(ascii_val - 32) # ASCII value of corresponding upper case letter
        else:
            upper_s += char # keep numeric characters and spaces as they are
    return upper_s