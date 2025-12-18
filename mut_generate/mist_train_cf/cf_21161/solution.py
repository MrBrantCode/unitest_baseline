"""
QUESTION:
Create a function called `check_equal` that takes two strings `s1` and `s2` as input and returns `True` if `s1` can be made equal to `s2` by replacing the letters with asterisks and numbers in the same order, and `False` otherwise. The numbers in `s2` should correspond to the number of times each letter appears consecutively in `s1`, and the letters can be grouped and repeated in any order within the asterisks. The function should handle strings that contain lowercase letters and digits, and it should assume that the input strings are valid and do not contain any unexpected characters.
"""

def check_equal(s1, s2):
    i = j = 0
    while i < len(s1) and j < len(s2):
        if s1[i] != s2[j]:
            return False
        count1 = count2 = 0
        while i < len(s1) and s1[i] == s2[j]:
            i += 1
            count1 += 1
        while j < len(s2) and (s2[j].isdigit() or s2[j] == '*'):
            if s2[j].isdigit():
                count2 = count2 * 10 + int(s2[j])
            j += 1
        if count1 != count2:
            return False
    return i == len(s1) and j == len(s2)