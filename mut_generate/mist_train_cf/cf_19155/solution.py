"""
QUESTION:
Write a recursive function `is_palindrome_recursive(s, left, right)` that checks if a given string `s` is a palindrome. The function should ignore any non-alphanumeric characters and be case-insensitive. It should have a time complexity of O(n^2), where n is the length of the input string. The function should not use any built-in string manipulation functions. Implement the function with a base case, and recursive calls to check the palindrome condition. The function `is_palindrome_recursive` should be called by `is_palindrome(s)` with initial `left` and `right` values as 0 and `len(s)-1` respectively.
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