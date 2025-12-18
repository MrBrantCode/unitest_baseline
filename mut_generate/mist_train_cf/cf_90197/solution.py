"""
QUESTION:
Construct a function named `check_strings` that takes two strings, `str1` and `str2`, as input. The function should return "Palindrome" if `str1` is a palindrome, "Not Palindrome" if `str1` is not a palindrome, and False otherwise. The strings should be checked under the following conditions: both `str1` and `str2` should have the same length and contain only lowercase alphabetic characters.
"""

def check_strings(str1, str2):
    if len(str1) == len(str2) and str1.islower() and str2.islower():
        if str1 == str1[::-1]:
            return "Palindrome"
        else:
            return "Not Palindrome"
    else:
        return False