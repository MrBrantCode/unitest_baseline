"""
QUESTION:
Write a function named `compare_strings` that takes two strings as input and returns "bigger", "smaller", or "equal" depending on their lexicographical order, ignoring case and leading/trailing whitespace. The function should not use built-in string comparison functions or sorting algorithms. The input strings will contain only alphabets and have lengths between 1 and 1000 (inclusive).
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