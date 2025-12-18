"""
QUESTION:
Implement a function `is_palindrome(s)` that checks if a given input string `s` is a palindrome. The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1), i.e., no extra space should be used. The function should not use any built-in functions or libraries that directly solve the problem and should perform case-insensitive comparison.
"""

def is_palindrome(s):
    # Convert the string to lowercase for case-insensitive comparison
    s = s.lower()

    # Initialize two pointers, one at the beginning and one at the end of the string
    left = 0
    right = len(s) - 1

    while left < right:
        # If the characters at the two pointers are not equal, the string is not a palindrome
        if s[left] != s[right]:
            return False

        # Move the pointers towards the middle
        left += 1
        right -= 1

    # All characters have been compared and they are equal, so the string is a palindrome
    return True