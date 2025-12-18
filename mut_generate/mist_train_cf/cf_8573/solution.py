"""
QUESTION:
Write a function `to_upper_case` that takes a string `s` containing only alphabetic characters as input and returns the string in upper case without using the built-in string method `upper()`, recursion, or iteration. The function should have a time complexity of O(n), where n is the length of the input string, and correctly handle both lowercase and uppercase alphabetic characters.
"""

def to_upper_case(s):
    upper_case = ""
    for char in s:
        char_code = ord(char)
        if 97 <= char_code <= 122:
            char_code -= 32
        upper_case += chr(char_code)
    return upper_case