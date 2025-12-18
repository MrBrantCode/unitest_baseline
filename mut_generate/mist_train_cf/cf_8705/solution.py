"""
QUESTION:
Implement a function named `compare_strings` that takes two strings as arguments and returns `True` if the strings are equal and `False` otherwise, without using built-in string comparison functions or operators. The function must have a time complexity of O(n), where n is the length of the longest string, and cannot use any additional data structures or functions.
"""

def compare_strings(string1, string2):
    # Check if the lengths of the strings are different
    if len(string1) != len(string2):
        return False
    
    # Compare each character of the strings
    for i in range(len(string1)):
        # Check if the characters are different
        if ord(string1[i]) != ord(string2[i]):
            return False
        
    return True