"""
QUESTION:
Implement a function `to_uppercase(string)` that takes a string as input and returns the string with all lowercase letters converted to uppercase. The function must not use any built-in methods for case conversion in Python. Instead, it should utilize ASCII character codes to perform the case conversion.
"""

def entrance(string):
    result = ""
    
    for char in string:
        ascii_code = ord(char)
        if 97 <= ascii_code <= 122:  # ASCII codes for lowercase letters
            ascii_code = ascii_code - 32  # Conversion to uppercase
        result += chr(ascii_code)
        
    return result