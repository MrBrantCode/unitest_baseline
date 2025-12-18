"""
QUESTION:
Create a function called `change_case` that takes a string as input and returns a new string where the case of each letter is swapped, without using any built-in case-changing functions. The time complexity of this function should be O(n), where n is the length of the input string. Non-alphabetical characters should remain unchanged.
"""

def change_case(string):
    result = ""
    for char in string:
        ascii_offset = 65 if 'A' <= char <= 'Z' else 97
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            result += chr(ascii_offset + (ord(char) - ascii_offset) ^ 32)
        else:
            result += char
    return result