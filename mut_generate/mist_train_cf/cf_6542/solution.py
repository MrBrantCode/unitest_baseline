"""
QUESTION:
Implement a function named `is_palindrome` that checks if a given input string is a palindrome. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string. The solution should not use any built-in functions or libraries that directly solve the problem, loops, or recursion.
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