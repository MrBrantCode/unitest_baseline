"""
QUESTION:
Write a function `compare_strings` that takes two strings as input and returns `True` if the strings are equal (ignoring leading and trailing white spaces) and `False` otherwise. The function should handle any printable ASCII characters, have a time complexity of O(n) where n is the length of the longer string after removing white spaces, and a space complexity of O(1).
"""

def compare_strings(str1, str2):
    # Removing leading and trailing white spaces
    str1 = str1.strip()
    str2 = str2.strip()
    
    # Comparing the lengths of the strings after removing white spaces
    if len(str1) != len(str2):
        return False
    
    # Comparing each character in the strings
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            return False
    
    return True