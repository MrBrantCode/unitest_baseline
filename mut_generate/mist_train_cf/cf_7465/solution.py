"""
QUESTION:
Write a function `is_palindrome` that takes a string as input and returns `True` if the string is a palindrome, ignoring any punctuation marks, spaces, and special characters, and considering it case-insensitive. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string, and it should handle strings with a length up to 10^6 characters.
"""

def is_palindrome(s: str) -> bool:
    # Convert the string to lowercase
    s = s.lower()

    # Define the set of valid characters
    valid_chars = set('abcdefghijklmnopqrstuvwxyz0123456789')

    # Initialize two pointers, one at the beginning and one at the end of the string
    left = 0
    right = len(s) - 1

    while left < right:
        # Move the left pointer to the next valid character
        while left < right and s[left] not in valid_chars:
            left += 1

        # Move the right pointer to the next valid character
        while left < right and s[right] not in valid_chars:
            right -= 1

        # Check if the characters at the pointers are equal
        if s[left] != s[right]:
            return False

        # Move the pointers towards the center
        left += 1
        right -= 1

    return True