"""
QUESTION:
Implement the `isPalindrome` function, which takes a string as input and returns `True` if the string is a palindrome (reads the same forward and backward, disregarding spaces, punctuation, and capitalization), and `False` otherwise.
"""

def isPalindrome(s: str) -> bool:
    s = ''.join(e for e in s if e.isalnum()).lower()
    return s == s[::-1]