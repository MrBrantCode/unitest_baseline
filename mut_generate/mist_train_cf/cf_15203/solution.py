"""
QUESTION:
Create a function named `is_anagram_palindrome` that takes two string parameters, `str1` and `str2`, and returns `True` if they are anagrams and both are palindromes, and `False` otherwise. The function should ignore spaces and capitalization, handle Unicode characters and special characters properly, and have a time complexity of O(n log n), where n is the length of the input strings.
"""

def is_anagram_palindrome(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    if len(str1) != len(str2):
        return False

    sorted_str1 = sorted(str1)
    sorted_str2 = sorted(str2)

    if sorted_str1 != sorted_str2:
        return False

    return str1 == str1[::-1] and str2 == str2[::-1]