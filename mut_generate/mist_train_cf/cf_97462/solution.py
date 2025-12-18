"""
QUESTION:
Write a function called `replace_with_ascii` that takes a string of alphabetic characters as input, replaces every character with its corresponding ASCII code, removes any duplicate ASCII codes, reverses the resulting list, and returns the reversed list as a string where each ASCII code is converted back to its corresponding character.
"""

def replace_with_ascii(string):
    ascii_codes = [ord(char) for char in string if ord(char) not in [ord(c) for c in string[:string.index(char)]]]
    ascii_codes.reverse()
    
    return ''.join(chr(code) for code in ascii_codes)