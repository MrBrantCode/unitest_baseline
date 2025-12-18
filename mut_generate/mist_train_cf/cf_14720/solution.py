"""
QUESTION:
Create a function called alternate_strings that takes two string parameters, str1 and str2. The function should return a new string consisting of alternating characters from str1 and str2. If one string is shorter than the other, append the remaining characters of the longer string to the end of the resulting string. However, if both strings are of the same length, do not include any characters from the second string in the resulting string.
"""

def alternate_strings(str1, str2):
    result = ''
    length = min(len(str1), len(str2))
    
    for i in range(length):
        result += str1[i] + str2[i]
    
    if len(str1) > len(str2):
        result += str1[length:]
    elif len(str2) > len(str1):
        result += str2[length:]
    
    return result