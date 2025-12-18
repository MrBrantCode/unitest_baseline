"""
QUESTION:
Write a function `count_palindrome_substrings` that takes a string `s` as input and returns the number of non-overlapping palindrome substrings found within `s` that are at least 3 characters long. The function should ignore non-alphanumeric characters and be case insensitive.
"""

def count_palindrome_substrings(s):
    """
    Returns the number of non-overlapping palindrome substrings found within `s` that are at least 3 characters long.
    Ignores non-alphanumeric characters and is case insensitive.

    :param s: Input string
    :return: Number of non-overlapping palindrome substrings
    """
    def is_palindrome(substring):
        """Check if a substring is palindrome."""
        substring = ''.join(c.lower() for c in substring if c.isalnum())
        return substring == substring[::-1]

    count = 0
    for i in range(len(s)):
        for j in range(i+3, len(s)+1):
            if is_palindrome(s[i:j]):
                count += 1
    return count