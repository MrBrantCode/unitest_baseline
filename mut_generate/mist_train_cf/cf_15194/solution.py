"""
QUESTION:
Create a function `is_palindrome(s)` that takes a string `s` as input and returns `True` if the string is a palindrome and `False` otherwise. The function should ignore any non-alphanumeric characters and consider the string case-insensitively. The function should use a constant amount of additional memory and have a time complexity of O(n), where n is the length of the input string.
"""

def entrance(s):
    # Remove spaces and punctuation marks, and convert to lowercase
    s = ''.join(e for e in s if e.isalnum()).lower()

    # Initialize pointers
    left = 0
    right = len(s) - 1

    # Iterate until pointers meet in the middle
    while left < right:
        # Compare characters at the two pointers
        if s[left] != s[right]:
            return False

        # Move pointers towards the middle
        left += 1
        right -= 1

    return True