"""
QUESTION:
Write a function named `compare_strings` that takes two parameters, `string1` and `string2`, and returns `True` if the strings are identical and `False` otherwise. The function should not use any built-in string comparison functions or libraries. It should only rely on the basic operations of iterating through the strings and comparing individual characters.
"""

def compare_strings(string1, string2):
    if len(string1) != len(string2):
        return False
    
    for i in range(len(string1)):
        if string1[i] != string2[i]:
            return False
    
    return True