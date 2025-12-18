"""
QUESTION:
Write a function named `is_palindrome` that takes a string `s` as input and returns a boolean value indicating whether the string is a palindrome or not, considering alphanumeric characters only and ignoring case sensitivity. The function should have a time complexity of O(n) and space complexity of O(1).
"""

def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        while not s[left].isalnum() and left < right:
            left += 1
        while not s[right].isalnum() and left < right:
            right -= 1

        if s[left].lower() != s[right].lower():
            return False

        left += 1
        right -= 1

    return True