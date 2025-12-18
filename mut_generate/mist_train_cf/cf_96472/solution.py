"""
QUESTION:
Write a function named `is_palindrome_recursive` that takes a string and two indices `start` and `end` as input, and returns `True` if the substring of the input string from index `start` to `end` is a palindrome and `False` otherwise. The function should use recursion to check for palindromes, and it should not use any extra space. The input string may contain at most 1000 characters, but the function should first be called with a string that has been converted to lowercase and had all whitespace removed.
"""

def is_palindrome_recursive(s, start, end):
    if start >= end:
        return True

    if s[start] != s[end]:
        return False

    return is_palindrome_recursive(s, start + 1, end - 1)