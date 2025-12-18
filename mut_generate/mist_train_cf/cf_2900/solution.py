"""
QUESTION:
Find the ASCII code for the character 'X' in a given string containing a mix of lowercase and uppercase letters, numbers, and special characters. Implement a function `find_ascii_code(string)` that has a time complexity of O(n), where n is the length of the string, and does not use built-in functions or libraries for ASCII code conversion.
"""

def find_ascii_code(string):
    for char in string:
        if char == 'X':
            return ord(char) - ord('0')
    return -1