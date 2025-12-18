"""
QUESTION:
Create a function named `is_one_away` that takes two strings as input and returns a boolean value indicating whether the first string is one character away from the second string. The function should consider case sensitivity and whitespace, and it should return False if the length difference between the two strings is greater than 1. The time complexity of the function should be O(n), where n is the length of the longer string.
"""

def is_one_away(str1, str2):
    str1 = str1.replace(" ", "")
    str2 = str2.replace(" ", "")

    if abs(len(str1) - len(str2)) > 1:
        return False

    if len(str1) == len(str2):
        diff_count = sum(1 for c1, c2 in zip(str1, str2) if c1 != c2)
        return diff_count == 1

    if len(str1) > len(str2):
        for i in range(len(str1)):
            if str1[:i] + str1[i+1:] == str2:
                return True
        return False

    if len(str1) < len(str2):
        for i in range(len(str2)):
            if str2[:i] + str2[i+1:] == str1:
                return True
        return False

    return False