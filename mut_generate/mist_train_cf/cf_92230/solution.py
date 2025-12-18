"""
QUESTION:
Create a function named `compareStrings` that takes two strings `str1` and `str2` as parameters. Compare the strings lexicographically and return 0 if they are equal, 1 if `str1` is greater, and -1 if `str2` is greater. If either string is empty, return -2. If both strings have the same length but differ in case, return -3. If both strings have the same characters but differ in the number of occurrences of a specific character, return -4. If any other error occurs during the comparison, return -5.
"""

def compareStrings(str1, str2):
    # Edge case 1: if either string is empty
    if len(str1) == 0 or len(str2) == 0:
        return -2
    
    # Edge case 2: if strings have same length but differ in case
    if len(str1) == len(str2) and str1.lower() == str2.lower():
        return -3
    
    # Edge case 3: if strings have same characters but differ in number of occurrences
    if sorted(str1) == sorted(str2) and str1 != str2:
        return -4
    
    try:
        # Compare the strings lexicographically
        if str1 < str2:
            return 1
        elif str1 > str2:
            return -1
        else:
            return 0
    except:
        # Handle any other error during comparison
        return -5