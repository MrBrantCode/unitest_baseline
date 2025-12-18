"""
QUESTION:
Write a function `camel_to_space(camel_str)` that takes a string containing only uppercase and lowercase letters as input, and returns the string with spaces inserted before each uppercase letter (except for the first letter) and all letters converted to lowercase. The function should have a time complexity of O(n) and a space complexity of O(n), where n is the length of the input string.
"""

def camel_to_space(camel_str):
    result = ""
    for i, char in enumerate(camel_str):
        if char.isupper() and i != 0:
            result += " "
        result += char.lower()
    return result