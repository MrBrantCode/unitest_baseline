"""
QUESTION:
Create a function called `replace_with_ascii` that takes a string as input. The function should return the string with every letter replaced by its corresponding ASCII character code. If the character is a lowercase letter, add 32 to its ASCII code before replacing. If the character is an uppercase letter, subtract 32 from its ASCII code before replacing. Non-alphabet characters should remain unchanged.
"""

def replace_with_ascii(string):
    result = ""
    for char in string:
        if char.islower():
            result += str(ord(char) + 32)
        elif char.isupper():
            result += str(ord(char) - 32)
        else:
            result += char
    return result