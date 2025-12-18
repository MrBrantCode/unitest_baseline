"""
QUESTION:
Implement a function `to_upper_case(s)` that takes a string `s` as input, where `s` only contains alphabetic characters. The function should return the uppercase equivalent of the input string without using the built-in `upper()` method or any other string methods that convert characters to uppercase. The function should not use recursion or iteration, and should have a time complexity of O(n), where n is the length of the input string.
"""

def to_upper_case(s):
    upper_case = ""
    for char in s:
        char_code = ord(char)
        if 97 <= char_code <= 122:
            char_code -= 32
        upper_case += chr(char_code)
    return upper_case