"""
QUESTION:
Create a function called `is_substring` that takes two strings `str1` and `str2` as input. Implement an algorithm that checks if `str2` is a substring of `str1` without using any built-in string searching functions or libraries. The function should handle cases where the input strings are empty, contain special characters, or are very long (over 1 million characters). Return "Yes" if `str2` is a substring of `str1`, and "No" otherwise.
"""

def entance(str1, str2):
    if not str1 or not str2:  # Check for empty strings
        return "No"
    
    if len(str1) < len(str2):  # Ensure str1 is longer or equal in length to str2
        str1, str2 = str2, str1
    
    for i in range(len(str1) - len(str2) + 1):  # Iterate through all possible substrings of str1
        if str1[i:i + len(str2)] == str2:  # Check if the current substring matches str2
            return "Yes"
    
    return "No"  # No matching substring found