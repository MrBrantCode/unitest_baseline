"""
QUESTION:
Write a function `is_one_away` that takes two strings as input and returns `True` if the first string is one character away from the second string, handling case sensitivity, whitespace, and punctuation, and considering a difference in length of more than 1 as `False`. The function should have a time complexity of O(n), where n is the length of the longer string.
"""

def is_one_away(str1, str2):
    # Remove whitespace and punctuation and convert to lowercase
    str1 = ''.join(e for e in str1 if e.isalnum()).lower()
    str2 = ''.join(e for e in str2 if e.isalnum()).lower()

    # Check length difference
    if abs(len(str1) - len(str2)) > 1:
        return False

    # Check for one character difference
    if len(str1) == len(str2):
        diff_count = 0
        for i in range(len(str1)):
            if str1[i] != str2[i]:
                diff_count += 1
            if diff_count > 1:
                return False
    else:
        # Make str1 the longer string
        if len(str1) < len(str2):
            str1, str2 = str2, str1

        diff_count = 0
        i = 0
        while i < len(str2):
            if str1[i + diff_count] != str2[i]:
                diff_count += 1
            if diff_count > 1:
                return False
            else:
                i += 1
        if diff_count == 0:
            diff_count += 1

    return diff_count == 1