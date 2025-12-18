"""
QUESTION:
Write a function `compare_strings` that takes two string parameters and returns `True` if they have the same content, ignoring any leading or trailing white spaces and any punctuation marks. The function should handle cases with special characters and have a time complexity of O(n), where n is the length of the longer string.
"""

import string

def compare_strings(str1, str2):
    # Remove leading and trailing white spaces
    str1 = str1.strip()
    str2 = str2.strip()
    
    # Remove punctuation marks from the strings
    str1 = str1.translate(str.maketrans("", "", string.punctuation))
    str2 = str2.translate(str.maketrans("", "", string.punctuation))
    
    # Compare the strings after removing leading/trailing white spaces and punctuation marks
    return str1 == str2