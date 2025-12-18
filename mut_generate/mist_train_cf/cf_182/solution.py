"""
QUESTION:
Write a function named `is_palindrome` that takes a string `s` as input, ignores any non-alphanumeric characters, and is case insensitive. The function should return the number of non-overlapping palindrome substrings found within the given string that are at least 5 characters long.
"""

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = ''.join(char.lower() for char in s if char.isalnum())

    count = 0

    for i in range(len(s)):
        # Check for palindrome substrings of at least 5 characters long
        if i + 4 < len(s) and s[i:i+5] == s[i:i+5][::-1]:
            count += 1
            i += 4

    return count