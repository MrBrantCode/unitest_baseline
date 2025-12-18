"""
QUESTION:
Write a function `compare_strings` that takes two strings `str1` and `str2` as input, where both strings contain only uppercase letters. The function should compare the two strings character by character using only bitwise operations, and return `True` if they are equal and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the longer string, and use a constant amount of additional space.
"""

def compare_strings(str1, str2):
    len1 = len(str1)
    len2 = len(str2)
    max_len = max(len1, len2)
    
    for i in range(max_len):
        if i >= len1 or i >= len2:
            return False
        
        char1 = ord(str1[i])
        char2 = ord(str2[i])
        
        if char1 ^ char2 != 0:
            return False
    
    return True