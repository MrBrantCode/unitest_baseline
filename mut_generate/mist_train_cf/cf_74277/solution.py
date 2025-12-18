"""
QUESTION:
Create a function called `reverse_concat` that takes two strings as input, reverses them, and then concatenates them in reverse order (i.e., the reversed second string followed by the reversed first string). The function should not use the "+" operator for concatenation.
"""

def reverse_concat(str1, str2):
    # Reverse the strings
    rev_str1 = str1[::-1]
    rev_str2 = str2[::-1]
    
    # Concatenate the strings
    concat_str = ''.join([rev_str2, rev_str1])
    return concat_str