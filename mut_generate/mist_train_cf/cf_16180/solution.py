"""
QUESTION:
Write a function named `is_palindrome` that takes a string as input and returns a boolean indicating whether the string is a palindrome, ignoring special characters but considering case sensitivity. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
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