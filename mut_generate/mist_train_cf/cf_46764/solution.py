"""
QUESTION:
Convert a given string of uppercase letters and spaces to lowercase using bitwise operators without utilizing built-in functions like lower() or casefold(). The function should take a string as input and return the string in lowercase. The ASCII value difference between uppercase and lowercase letters should be considered in the solution.
"""

def entrance(s):
    result = []
    for char in s:
        if 'A' <= char <= 'Z':
            # 32 is the difference between the ASCII values of 'a' and 'A'
            result.append(chr(ord(char) | 32))
        else:
            result.append(char)
    return ''.join(result)