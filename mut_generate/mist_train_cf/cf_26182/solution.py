"""
QUESTION:
Create a function named `alt_string` that takes two strings `str1` and `str2` as input and returns a new string consisting of alternating characters from `str1` and `str2`. If the strings are of different lengths, append the remaining characters from the longer string to the end of the result.
"""

def alt_string(str1, str2):
    alt_str = "" 
    length = len(str1) if len(str1) <= len(str2) else len(str2)
    
    for i in range(length):
        alt_str += str1[i] + str2[i]
    
    if len(str1) > len(str2):
        alt_str += str1[length:]
    elif len(str2) > len(str1):
        alt_str += str2[length:]
    
    return alt_str