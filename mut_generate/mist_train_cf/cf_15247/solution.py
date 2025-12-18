"""
QUESTION:
Write a function `is_palindrome` that takes a string as input and returns a boolean indicating whether the string is a palindrome or not. The function should ignore non-alphabetic characters, be case-insensitive, and consider numbers and special characters as part of the palindrome check. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def is_palindrome(string):
    # Initialize two pointers, one starting from the beginning of the string and the other from the end
    left = 0
    right = len(string) - 1

    while left < right:
        # Move the left pointer until an alphabetic character is found
        while left < right and not string[left].isalpha():
            left += 1

        # Move the right pointer until an alphabetic character is found
        while left < right and not string[right].isalpha():
            right -= 1

        # If the characters at the two pointers are not equal, the string is not a palindrome
        if left < right and string[left].lower() != string[right].lower():
            return False

        # Move the pointers towards the center
        left += 1
        right -= 1

    # All characters were checked and they were equal, so the string is a palindrome
    return True