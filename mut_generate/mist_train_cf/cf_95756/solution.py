"""
QUESTION:
Create a function called `compareStrings` that takes two strings `str1` and `str2` as parameters and returns an integer indicating their lexicographic comparison result. The function should return 0 if the strings are equal, 1 if `str1` is greater, and -1 if `str2` is greater. The function should also handle the following edge cases: 
- Return -2 if either string is empty.
- Return -3 if the strings have the same length but differ in case.
- Return -4 if the strings have the same characters but differ in the number of occurrences of a specific character.
- Return -5 if any other error occurs during the comparison.
The function should have a time complexity of O(n), where n is the length of the longer string.
"""

def compareStrings(str1, str2):
    # Edge case 1: if either of the strings is empty
    if str1 == "" or str2 == "":
        return -2

    # Edge case 2: if both strings have the same length but differ in case
    if str1.lower() == str2.lower() and str1 != str2:
        return -3

    # Edge case 3: if both strings have the same characters but differ in the number of occurrences of a specific character
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
        # Edge case 4: handle any other error
        return -5