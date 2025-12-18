"""
QUESTION:
Write a function `is_palindrome(s)` that checks whether the input string `s` is a palindrome or not. The function should handle case-insensitive nature of palindromes, punctuation, whitespace, and numbers. The solution must be in-place with constant extra space and have a time complexity of O(n), where n is the length of the input string.
"""

def is_palindrome(s):
    # Convert the string to lowercase
    s = s.lower()

    # Remove punctuation and whitespace from the string
    s = ''.join(c for c in s if c.isalnum())

    # Initialize two pointers, one at the start of the string and the other at the end
    i = 0
    j = len(s) - 1

    # Loop through the string, comparing characters at the two pointers
    while i < j:
        # If the characters are not equal, return False
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1

    # If the loop completes without returning False, the string is a palindrome
    return True