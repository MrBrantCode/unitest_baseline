"""
QUESTION:
Create a function named `concatenate_strings` that takes two strings `str1` and `str2` as parameters. The function should return a concatenated string where each character from `str1` is followed by its corresponding character from `str2`. If `str1` and `str2` are not of equal length, the remaining characters from the longer string should be appended to the end of the concatenated string. The function should have a time complexity of O(n), where n is the length of the longer string.
"""

def concatenate_strings(str1, str2):
    # Determine the lengths of the two strings
    len1 = len(str1)
    len2 = len(str2)
    
    # Initialize an empty list to store the concatenated characters
    result = []
    
    # Iterate through the characters of the longer string
    for i in range(max(len1, len2)):
        # If the index is within the length of the first string, add its character to the result list
        if i < len1:
            result.append(str1[i])
        # If the index is within the length of the second string, add its character to the result list
        if i < len2:
            result.append(str2[i])
    
    # Join the characters in the result list to form the final concatenated string
    return ''.join(result)