"""
QUESTION:
Create a function called `is_anagram_palindrome` that takes two string parameters and returns `True` if they are anagrams and palindromes, and `False` otherwise. The function should ignore any spaces and capitalization, handle Unicode characters and special characters properly, and have a time complexity of O(n log n), where n is the length of the input strings. The function should not use any built-in functions or libraries that directly solve the anagram problem.
"""

import re

def is_anagram_palindrome(str1, str2):
    # Remove spaces and punctuation marks using a regular expression
    str1 = re.sub(r'[^\w\s]', '', str1)
    str2 = re.sub(r'[^\w\s]', '', str2)

    # Convert both strings to lowercase
    str1 = str1.lower()
    str2 = str2.lower()

    # Sort both strings
    str1 = sorted(str1)
    str2 = sorted(str2)

    # Compare the sorted strings
    if str1 == str2:
        return True
    else:
        return False