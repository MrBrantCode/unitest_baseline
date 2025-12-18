"""
QUESTION:
Implement the `is_palindrome` function to check if a given string is a palindrome, ignoring any punctuation marks, spaces, and special characters. The function should be case-insensitive and have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string. The input string can have up to 10^6 characters.
"""

def is_palindrome(input_string):
    input_string = input_string.lower()
    valid_chars = set('abcdefghijklmnopqrstuvwxyz0123456789')
    left = 0
    right = len(input_string) - 1

    while left < right:
        while left < right and input_string[left] not in valid_chars:
            left += 1

        while left < right and input_string[right] not in valid_chars:
            right -= 1

        if input_string[left] != input_string[right]:
            return False

        left += 1
        right -= 1

    return True