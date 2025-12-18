"""
QUESTION:
Implement a function `is_palindrome_recursive` to determine if a given string `s` is a palindrome, considering only alphanumeric characters and ignoring case sensitivity, spaces, special characters, and punctuation marks. The function should not use any built-in string manipulation functions or regular expressions and should have a time complexity of O(n), where n is the length of the string.
"""

def is_palindrome_recursive(s):
    def is_alphanumeric(c):
        return c.isalpha() or c.isdigit()
    
    def is_palindrome_recursive(s, left, right):
        if left >= right:
            return True
        if not is_alphanumeric(s[left]):
            return is_palindrome_recursive(s, left + 1, right)
        if not is_alphanumeric(s[right]):
            return is_palindrome_recursive(s, left, right - 1)
        if s[left].lower() != s[right].lower():
            return False
        return is_palindrome_recursive(s, left + 1, right - 1)

    return is_palindrome_recursive(s, 0, len(s) - 1)