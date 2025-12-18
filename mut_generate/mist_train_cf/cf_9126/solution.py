"""
QUESTION:
Write a function `compare_strings` that takes two strings as input and returns a boolean indicating whether the strings are equal, considering case sensitivity and whitespace, without using any built-in string comparison functions or methods.
"""

def compare_strings(string1, string2):
    # Check if the lengths of the strings are equal
    if len(string1) != len(string2):
        return False
    
    # Iterate through each character of both strings
    for i in range(len(string1)):
        # Check if the characters are different
        if string1[i] != string2[i]:
            return False
    
    # All characters are equal
    return True