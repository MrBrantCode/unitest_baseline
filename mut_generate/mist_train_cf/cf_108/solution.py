"""
QUESTION:
Write a function named `is_palindrome` that checks whether a given input string is a palindrome or not. The function should have a time complexity of O(n), where n is the length of the input string, and should use constant extra space. The function should handle case-insensitive palindromes, ignore punctuation and whitespace, and work with alphanumeric characters, including numbers. The function should be able to handle strings with a length of up to 10^6.
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