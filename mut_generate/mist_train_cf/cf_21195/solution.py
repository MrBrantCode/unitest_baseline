"""
QUESTION:
Create a function `is_palindrome_recursive` that checks if a given string is a palindrome or not without using extra space, ignoring case sensitivity, and only using recursion. The input string has at most 1000 characters and may contain whitespace. The function should take three parameters: the input string, and two indices (start and end) representing the current substring being checked.
"""

def is_palindrome_recursive(s, i, j):
    # Base case: if start and end meet or cross each other, it is a palindrome
    if i >= j:
        return True

    # Check if characters at start and end indices are equal
    if s[i].lower() != s[j].lower():
        return False

    # Recursively check the remaining substring
    return is_palindrome_recursive(s, i + 1, j - 1)