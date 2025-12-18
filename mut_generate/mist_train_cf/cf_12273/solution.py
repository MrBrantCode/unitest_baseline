"""
QUESTION:
Create a function named `compareStrings` that takes two strings as parameters and compares them. Return 0 if the strings are equal, 1 if the first string is greater (based on lexicographic order), and -1 if the second string is greater. The function should also handle the following edge cases: 

- Return -2 if either of the input strings is empty. 
- Return -3 if both strings have the same length but differ in case.
- Return -4 if both strings have the same characters but differ in the number of occurrences of a specific character.
- Return -5 if any other error occurs during the comparison.
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
            return -1
        elif str1 > str2:
            return 1
        else:
            return 0
    except:
        # Handle any other error during comparison
        return -5