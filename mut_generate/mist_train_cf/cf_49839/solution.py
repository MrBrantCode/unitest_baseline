"""
QUESTION:
Implement the `is_palindrome` function to determine if a given string is a palindrome and the `make_palindrome` function to find the shortest possible palindrome that begins with the provided string. The `make_palindrome` function should follow this algorithm: 

1. Find the longest postfix of the supplied string that is a palindrome.
2. Reverse the string prefix that comes before the palindromic suffix, and append it to the end of the original string to create the shortest possible palindrome.

Do not import any additional modules or libraries. The functions should work with the following restrictions and examples:

- `is_palindrome` function should return a boolean value.
- `make_palindrome` function should return a string.
- `make_palindrome('')` should return an empty string `''`.
- `make_palindrome('cat')` should return `'catac'`.
- `make_palindrome('cata')` should return `'catac'`.
"""

def is_palindrome(string: str) -> bool:
    """ Test if given string is a palindrome """
    return string == string[::-1]


def make_palindrome(s: str) -> str:
    """ Find the shortest palindrome that begins with a supplied string.
    Algorithm idea is simple:
    - Find the longest postfix of supplied string that is a palindrome.
    - Append to the end of the string reverse of a string prefix that comes before the palindromic suffix.
    """
    if is_palindrome(s):
        return s

    for i in range(len(s)):
        if is_palindrome(s[i:]):
            reversed_prefix = s[:i][::-1]
            return s + reversed_prefix

    return s + s[::-1]