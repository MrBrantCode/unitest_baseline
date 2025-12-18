"""
QUESTION:
Implement a function `is_palindrome(string)` that takes a string as input and returns `True` if the string is a palindrome, considering only alphabetic characters, and `False` otherwise. The function should ignore non-alphabetic characters and be case-insensitive. The time complexity should be O(n) and the space complexity should be O(1), where n is the length of the string.
"""

def is_palindrome(string):
    left = 0
    right = len(string) - 1

    while left <= right:
        if not string[left].isalpha():
            left += 1
            continue

        if not string[right].isalpha():
            right -= 1
            continue

        if string[left].lower() != string[right].lower():
            return False

        left += 1
        right -= 1

    return True