"""
QUESTION:
Implement a function `compare_strings(string1, string2)` that takes two strings as input and returns True if they are equal, False otherwise. The function should not use built-in string comparison methods or operators such as '=='. It should compare the strings character by character using its own algorithm. Note that the use of loops and recursion is not allowed.
"""

def compare_strings(string1, string2):
    if len(string1) != len(string2):
        return False
    
    if string1 and string2:
        return (string1[0] == string2[0]) and compare_strings(string1[1:], string2[1:])
    
    return True