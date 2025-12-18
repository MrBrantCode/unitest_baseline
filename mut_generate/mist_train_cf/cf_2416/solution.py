"""
QUESTION:
Write a function `is_palindrome_recursive` that checks if a given string is a palindrome, ignoring case sensitivity and non-alphanumeric characters, with a time complexity of O(n) and a space complexity of O(1) using a recursive approach. The function should return a boolean value indicating whether the string is a palindrome or not.
"""

def is_palindrome_recursive(s):
    # Base case: if the string is empty or contains only one character, it is a palindrome
    if len(s) <= 1:
        return True

    # Convert the string to lowercase
    s = s.lower()

    # Check if the first and last characters are alphanumeric
    if not s[0].isalnum():
        return is_palindrome_recursive(s[1:])
    if not s[-1].isalnum():
        return is_palindrome_recursive(s[:-1])

    # If the first and last characters are equal, recursively check the substring excluding the start and end characters
    if s[0] == s[-1]:
        return is_palindrome_recursive(s[1:-1])
    
    # If the first and last characters are not equal, it is not a palindrome
    return False