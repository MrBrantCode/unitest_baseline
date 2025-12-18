"""
QUESTION:
Create a function `combine_strings` that takes two strings `str1` and `str2` as input and returns a new string where the characters from both strings are combined in an alternating manner. If the strings have different lengths, the remaining characters from the longer string should be appended to the end of the result. The function must not use any built-in string concatenation functions or operators (such as +).
"""

def entance(str1, str2):
    combined = ""
    length = min(len(str1), len(str2))
    
    for i in range(length):
        combined += str1[i] + str2[i]
    
    if len(str1) > len(str2):
        combined += str1[length:]
    elif len(str2) > len(str1):
        combined += str2[length:]
    
    return combined