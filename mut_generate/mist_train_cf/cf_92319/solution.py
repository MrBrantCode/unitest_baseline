"""
QUESTION:
Create a function `replace_A_with_Z` that replaces all instances of 'A' and 'a' in a given string with 'Z' and 'z' respectively, preserving the original case sensitivity. The function should have a time complexity of O(n), where n is the length of the string.
"""

def replace_A_with_Z(string):
    new_string = ""
    for char in string:
        if char == 'A':
            new_string += 'Z'
        elif char == 'a':
            new_string += 'z'
        else:
            new_string += char
    return new_string