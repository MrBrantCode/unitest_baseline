"""
QUESTION:
Create a function called `is_palindrome` that takes a string as input and returns `True` if the string is a palindrome (ignoring non-alphabetic characters and considering alphabetic characters in a case-insensitive manner) and `False` otherwise. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string.
"""

def is_palindrome(s: str) -> bool:
    left = 0
    right = len(s) - 1

    while left <= right:
        if not s[left].isalpha():
            left += 1
            continue

        if not s[right].isalpha():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True