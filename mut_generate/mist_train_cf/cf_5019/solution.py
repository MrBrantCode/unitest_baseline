"""
QUESTION:
Implement a function named `compareStrings` that compares two input strings in a case-insensitive and lexicographical manner. The function should handle null inputs and have a time complexity of O(n), where n is the length of the longer string. The function should also have a space complexity of O(1), meaning it should not use any additional data structures to perform the comparison. The function should return an integer indicating the result of the comparison: -1 if the first string is lexicographically less than the second, 1 if the first string is lexicographically greater than the second, and 0 if the strings are equal.
"""

def compareStrings(str1, str2):
    # Error handling for null inputs
    if str1 is None and str2 is None:
        return 0
    elif str1 is None:
        return -1
    elif str2 is None:
        return 1

    len1 = len(str1)
    len2 = len(str2)
    index = 0

    while index < len1 and index < len2:
        ch1 = str1[index].lower()
        ch2 = str2[index].lower()

        if ch1 < ch2:
            return -1
        elif ch1 > ch2:
            return 1

        index += 1

    if len1 < len2:
        return -1
    elif len1 > len2:
        return 1

    return 0