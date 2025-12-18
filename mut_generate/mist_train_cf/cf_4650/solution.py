"""
QUESTION:
Define a function `compare_strings(str1, str2)` that compares two strings using only bitwise operations. The strings are guaranteed to contain only uppercase letters and the function should have a time complexity of O(n), where n is the length of the longer string. Additionally, the function should use a constant amount of additional space.
"""

def entrance(str1, str2):
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