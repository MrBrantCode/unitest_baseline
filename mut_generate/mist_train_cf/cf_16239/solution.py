"""
QUESTION:
Implement a function `combine_strings(str1, str2)` that takes two strings as input and returns a single string that combines the input strings by alternating characters from both strings. If one string is longer than the other, append the remaining characters from the longer string to the end of the combined string. Do not use any built-in string concatenation functions or operators.
"""

def entrance(str1, str2):
    combined = ""
    length = min(len(str1), len(str2))
    
    for i in range(length):
        combined += str1[i] + str2[i]
    
    if len(str1) > len(str2):
        combined += str1[length:]
    elif len(str2) > len(str1):
        combined += str2[length:]
    
    return combined