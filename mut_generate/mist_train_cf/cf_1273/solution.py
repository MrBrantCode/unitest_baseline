"""
QUESTION:
Create a function called `combine_strings` that takes two strings as input and returns a new string. The function should not use any built-in string concatenation functions or operators. The resulting string should alternate characters from the two input strings, starting with the first character of the first string, then the first character of the second string, then the second character of the first string, and so on. If one string is longer than the other, append the remaining characters of the longer string to the end of the resulting string.
"""

def combine_strings(str1, str2):
    combined_string = ""
    length = min(len(str1), len(str2))
    
    for i in range(length):
        combined_string += str1[i] + str2[i]
    
    if len(str1) > len(str2):
        combined_string += str1[length:]
    else:
        combined_string += str2[length:]
    
    return combined_string