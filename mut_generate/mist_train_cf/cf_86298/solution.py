"""
QUESTION:
Write a function `is_palindrome(s)` that checks if a given string `s` contains non-overlapping palindrome substrings of at least 5 characters long, ignoring non-alphanumeric characters and case sensitivity. Return the number of such palindrome substrings.
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