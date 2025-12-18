"""
QUESTION:
Implement the function `convert_case(s)` that takes a string `s` as input, and returns a new string where all lowercase characters are converted to uppercase and all uppercase characters are converted to lowercase. Characters that are neither lowercase nor uppercase should remain unchanged. The function should have a time complexity of O(n), where n is the length of the input string, and should not use built-in functions or methods that directly convert characters to uppercase or lowercase. The function should handle strings containing Unicode characters, and should be case-sensitive and able to handle leading and trailing spaces and empty strings correctly.
"""

def convert_case(s):
    converted = ""
    for char in s:
        if char.islower():
            converted += chr(ord(char) - 32)
        elif char.isupper():
            converted += chr(ord(char) + 32)
        else:
            converted += char
    return converted