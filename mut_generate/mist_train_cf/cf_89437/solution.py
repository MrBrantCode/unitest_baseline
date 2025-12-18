"""
QUESTION:
Create a function called `is_palindrome` that takes a string as input and returns `True` if the string is a palindrome and `False` otherwise. The function must meet the following requirements:

- The function should have a time complexity of O(n), where n is the length of the string.
- The function should not use any built-in string reversal functions or methods.
- The function should not use any additional data structures except for temporary variables if necessary.
- The function should be case-insensitive and consider alphanumeric characters only, ignoring other characters.
- The function should handle non-Latin characters.
- The function should not use string comparison functions or methods to check character equality.
"""

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    left, right = 0, len(s) - 1

    while left < right:
        if not s[left].isalnum():
            left += 1
            continue
        if not s[right].isalnum():
            right -= 1
            continue

        if s[left].lower() != s[right].lower():
            return False
        left += 1
        right -= 1
    return True