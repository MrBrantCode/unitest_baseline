"""
QUESTION:
Write a function `replace_A_with_Z` that takes a string as input and returns a new string where all instances of 'A' are replaced with 'Z' and all instances of 'a' are replaced with 'z', preserving the original case sensitivity. The function should have a time complexity of O(n), where n is the length of the string.
"""

def replace_A_with_Z(s):
    new_string = ""
    for char in s:
        if char == 'A':
            new_string += 'Z'
        elif char == 'a':
            new_string += 'z'
        else:
            new_string += char
    return new_string