"""
QUESTION:
Implement a function `change_case` that takes a string as input and returns a new string with the case of each letter toggled (i.e., uppercase becomes lowercase and vice versa). The function should have a time complexity of O(n), where n is the length of the string, and should not use any built-in string case conversion functions or conditional statements for changing the case of each character.
"""

def change_case(s):
    """
    Toggle the case of each letter in a string.

    Args:
        s (str): The input string.

    Returns:
        str: A new string with the case of each letter toggled.
    """
    result = ""
    for char in s:
        ascii_val = ord(char)
        if ascii_val >= 97 and ascii_val <= 122:  # lowercase letters
            result += chr(ascii_val - 32)
        elif ascii_val >= 65 and ascii_val <= 90:  # uppercase letters
            result += chr(ascii_val + 32)
        else:
            result += char
    return result