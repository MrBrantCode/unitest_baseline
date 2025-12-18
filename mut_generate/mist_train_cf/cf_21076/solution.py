"""
QUESTION:
Write a function named `compare_strings` that takes two strings as input and returns the index of the first character that is unequal in the two strings. You cannot use built-in string comparison functions or operators like "==" and "!=". If one string ends before the other, return the length of the smaller string.
"""

def compare_strings(string1, string2):
    index = 0
    while index < len(string1) and index < len(string2):
        if string1[index] != string2[index]:
            return index
        index += 1
    
    if len(string1) < len(string2):
        return len(string1)
    elif len(string2) < len(string1):
        return len(string2)
    
    return len(string1)