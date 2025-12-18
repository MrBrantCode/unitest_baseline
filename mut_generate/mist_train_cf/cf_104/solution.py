"""
QUESTION:
Write a function called `is_anagram_palindrome` that takes two strings as input and returns True if they are anagrams and palindromes, ignoring any spaces and capitalization. The function should have a time complexity of O(n log n), where n is the length of the input strings, and should not use any built-in functions or libraries that directly solve the anagram problem. Assume that the input strings will only contain alphanumeric characters, spaces, and punctuation marks.
"""

def is_anagram_palindrome(str1, str2):
    # Remove spaces and punctuation marks using a regular expression
    str1 = ''.join(e for e in str1 if e.isalnum()).lower()
    str2 = ''.join(e for e in str2 if e.isalnum()).lower()

    # Sort both strings
    str1 = sorted(str1)
    str2 = sorted(str2)

    # Compare the sorted strings
    return str1 == str2