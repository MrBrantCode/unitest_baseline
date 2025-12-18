"""
QUESTION:
Write a function named `to_uppercase` that takes a string as input and returns a new string with all characters converted to uppercase. The function cannot use any built-in string conversion methods. The input string can contain a mix of letters and non-alphabetic characters, and the function should only convert the lowercase letters to uppercase.
"""

def entrance(s):
    result = ""
    for char in s:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - ord('a') + ord('A'))
        else:
            result += char
    return result