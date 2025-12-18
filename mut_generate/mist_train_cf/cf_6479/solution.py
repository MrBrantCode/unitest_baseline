"""
QUESTION:
Create a function named `is_palindrome` that takes a string as input and returns `True` if the string is a palindrome, otherwise returns `False`. The function should be case-insensitive, consider alphanumeric characters only, ignore non-alphanumeric characters, handle non-Latin characters, and have a time complexity of O(n). The function cannot use built-in string reversal functions or methods, additional data structures (except temporary variables), or string comparison functions to check character equality.
"""

def is_palindrome(string):
    left = 0
    right = len(string) - 1

    while left < right:
        if not string[left].isalnum():
            left += 1
        elif not string[right].isalnum():
            right -= 1
        elif string[left].lower() != string[right].lower():
            return False
        else:
            left += 1
            right -= 1

    return True