"""
QUESTION:
Write a function named `is_palindrome` that takes a string as input and returns a boolean indicating whether the string is a palindrome or not. The function should ignore non-alphabetic characters, be case-insensitive, and consider numbers and special characters as part of the palindrome check. The time complexity should be O(n), where n is the length of the input string, and the space complexity should be O(1).
"""

def is_palindrome(s):
    # Initialize two pointers, one starting from the beginning of the string and the other from the end
    left = 0
    right = len(s) - 1

    while left < right:
        # Move the left pointer until an alphabetic character is found
        while left < right and not s[left].isalpha():
            left += 1

        # Move the right pointer until an alphabetic character is found
        while left < right and not s[right].isalpha():
            right -= 1

        # If the characters at the two pointers are not equal, the string is not a palindrome
        if left < right and s[left].lower() != s[right].lower():
            return False

        # Move the pointers towards the center
        left += 1
        right -= 1

    # All characters were checked and they were equal, so the string is a palindrome
    return True