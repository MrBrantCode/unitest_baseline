"""
QUESTION:
Write a function called `change_case` that takes a string as input, swaps the case of each alphabetic character (i.e., lowercase becomes uppercase and vice versa), and leaves non-alphabetic characters unchanged. The function should have a time complexity of O(n), where n is the length of the string, and should not use any built-in functions or methods specifically designed for changing the case of strings.
"""

def change_case(s):
    result = ""
    for char in s:
        if char.islower():
            result += char.upper()
        elif char.isupper():
            result += char.lower()
        else:
            result += char
    return result