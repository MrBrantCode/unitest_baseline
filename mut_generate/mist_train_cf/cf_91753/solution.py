"""
QUESTION:
Create a function `replace_with_ascii` that takes a string as input, replaces every letter with its corresponding modified ASCII character code (add 32 to the ASCII code for lowercase letters, subtract 32 for uppercase letters), and leaves non-letter characters unchanged. Return the resulting string.
"""

def replace_with_ascii(string):
    result = ""
    for char in string:
        if char.islower():
            result += chr(ord(char) + 32)
        elif char.isupper():
            result += chr(ord(char) - 32)
        else:
            result += char
    return result