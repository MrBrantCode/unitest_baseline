"""
QUESTION:
Implement a recursive function `is_palindrome_recursive` that determines if a given string `s` is a palindrome, ignoring non-alphanumeric characters and considering only alphanumeric characters with case insensitivity. The function should not use any built-in string manipulation functions or regular expressions and should have a time complexity of O(n), where n is the length of the string `s`.
"""

def is_palindrome_recursive(s, left=0, right=None):
    if right is None:
        right = len(s) - 1

    # Base case: if left pointer is greater than or equal to right pointer, it is a palindrome
    if left >= right:
        return True

    # If left character is not alphanumeric, move left pointer one step forward
    if not (s[left].isalpha() or s[left].isdigit()):
        return is_palindrome_recursive(s, left + 1, right)

    # If right character is not alphanumeric, move right pointer one step backward
    if not (s[right].isalpha() or s[right].isdigit()):
        return is_palindrome_recursive(s, left, right - 1)

    # If left and right characters are alphanumeric and not equal, it is not a palindrome
    if s[left].lower() != s[right].lower():
        return False

    # Recursive call with updated pointers
    return is_palindrome_recursive(s, left + 1, right - 1)