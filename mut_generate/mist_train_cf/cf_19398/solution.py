"""
QUESTION:
Write a function named `compare_strings` that takes two strings `s1` and `s2` as input and returns a boolean value indicating whether they are equal. The function should only use bitwise operations, have a time complexity of O(n) where n is the length of the longer string, and use a constant amount of additional space.
"""

def entrance(s1, s2):
    n = max(len(s1), len(s2))
    
    for i in range(n):
        if i < len(s1) and i < len(s2):
            if ord(s1[i]) ^ ord(s2[i]):
                return False
        else:
            return False
    
    return True