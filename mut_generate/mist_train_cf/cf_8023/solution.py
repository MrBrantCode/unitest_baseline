"""
QUESTION:
Create a function `compare_strings` that compares two strings lexicographically and returns "bigger", "smaller", or "equal" depending on their order. The comparison should be case-insensitive and ignore leading/trailing whitespace characters. The input strings will only contain alphabets with lengths between 1 and 1000 (inclusive). Do not use built-in string comparison functions or sorting algorithms.
"""

def compare_strings(str1, str2):
    # Remove leading and trailing whitespace
    str1 = str1.strip()
    str2 = str2.strip()
    
    # Make both strings lowercase
    str1 = str1.lower()
    str2 = str2.lower()
    
    # Compare each character of the strings
    for i in range(min(len(str1), len(str2))):
        if str1[i] < str2[i]:
            return "smaller"
        elif str1[i] > str2[i]:
            return "bigger"
    
    # If all characters are equal, compare the lengths of the strings
    if len(str1) < len(str2):
        return "smaller"
    elif len(str1) > len(str2):
        return "bigger"
    else:
        return "equal"