"""
QUESTION:
Write a function `compare_strings` that takes two string arguments and returns `True` if they match, considering both case-sensitive and case-insensitive comparisons, and `False` otherwise.
"""

def compare_strings(str1, str2):
    # Case-sensitive comparison
    if str1 == str2:
        return True
    
    # Case-insensitive comparison
    if str1.lower() == str2.lower():
        return True
    
    return False