"""
QUESTION:
Write a function `count_palindrome_substrings` that takes a string `s` as input. This function should return the number of palindrome substrings in `s` that are at least 3 characters long, do not overlap with each other, and ignore non-alphanumeric characters. The function should also be case insensitive.
"""

def count_palindrome_substrings(s):
    def is_palindrome(substring):
        substring = ''.join(c.lower() for c in substring if c.isalnum())
        return substring == substring[::-1]

    count = 0
    for i in range(len(s)):
        for j in range(i+3, len(s)+1):
            if is_palindrome(s[i:j]):
                count += 1
    return count