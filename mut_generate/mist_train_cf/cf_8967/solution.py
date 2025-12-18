"""
QUESTION:
Write a function `isPalindrome(s)` to check if a given string `s` is a palindrome or not, ignoring non-alphanumeric characters and considering case-insensitivity. The function must have a time complexity of O(n), where n is the length of the input string, and use constant extra space without any additional data structures.
"""

def entance(s):
    s = s.lower()
    left = 0
    right = len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        else:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1
    return True