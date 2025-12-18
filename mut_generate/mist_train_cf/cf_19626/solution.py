"""
QUESTION:
Create a function `compareStrings` that takes two non-null strings `str1` and `str2` as parameters. The function should compare the strings lexicographically and return 0 if they are equal, 1 if `str1` is greater, and -1 if `str2` is greater. The function should also handle the following edge cases: return -2 if either string is empty, -3 if both strings have the same length but differ in case, and -4 if both strings have the same characters but differ in the number of occurrences of a specific character. The function should return -5 for any other error. The time complexity should be O(n), where n is the length of the longer string.
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
            return -1
        elif str1 > str2:
            return 1
        else:
            return 0
    except:
        # Edge case 4: handle any other error
        return -5