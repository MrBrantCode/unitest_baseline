"""
QUESTION:
Write a function `compare_strings` that takes two string parameters, `string1` and `string2`. The function should compare the two strings and return the index of the first character that is unequal in the two strings. If one string ends before the other, return the length of the smaller string. Do not use any built-in string comparison functions or operators.
"""

def compare_strings(string1, string2):
    index = 0
    while index < len(string1) and index < len(string2):
        if string1[index] != string2[index]:
            return index
        index += 1
    
    # Check if one string ends before the other
    if len(string1) < len(string2):
        return len(string1)
    elif len(string2) < len(string1):
        return len(string2)
    
    # If the loop completes without finding a mismatch
    return len(string1)