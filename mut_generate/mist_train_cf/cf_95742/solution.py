"""
QUESTION:
Write a function `is_one_away(str1, str2)` that takes two strings as input and returns True if the first string is one character away from the second string, considering case sensitivity and whitespace. The function should return False if the two strings have a difference in length greater than 1. The time complexity of the function should be O(n), where n is the length of the longer string.
"""

def is_one_away(str1, str2):
    # If the length difference is greater than 1, return False
    if abs(len(str1) - len(str2)) > 1:
        return False

    # If the strings have the same length, check if there is only one differing character
    if len(str1) == len(str2):
        diff_count = sum(1 for c1, c2 in zip(str1, str2) if c1 != c2)
        return diff_count == 1

    # If the first string is longer, check if there is only one character that needs to be removed
    if len(str1) > len(str2):
        for i in range(len(str1)):
            temp = str1[:i] + str1[i + 1:]
            if temp == str2:
                return True
        return False

    # If the second string is longer, check if there is only one character that needs to be added
    if len(str1) < len(str2):
        for i in range(len(str2)):
            temp = str2[:i] + str2[i + 1:]
            if temp == str1:
                return True
        return False