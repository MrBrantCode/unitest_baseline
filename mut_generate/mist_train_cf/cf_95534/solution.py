"""
QUESTION:
Implement a recursive function `is_palindrome_recursive(s, left, right)` that determines whether the input string `s` is a palindrome, ignoring non-alphanumeric characters and considering the comparison case-insensitive. The function must have a time complexity of O(n^2), where n is the length of the input string, and must not use any built-in string manipulation functions.
"""

def is_palindrome_recursive(s, left, right):
    # Base case
    if left >= right:
        return True

    # Check if left and right characters are alphanumeric
    if not s[left].isalnum():
        return is_palindrome_recursive(s, left+1, right)
    if not s[right].isalnum():
        return is_palindrome_recursive(s, left, right-1)

    # Check if left and right characters are equal (case-insensitive)
    if s[left].lower() != s[right].lower():
        return False

    # Recursively call with updated left and right values
    return is_palindrome_recursive(s, left+1, right-1)