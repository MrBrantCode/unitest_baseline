"""
QUESTION:
Create a function named `is_palindrome` that determines if a given string is a palindrome. The function should consider only alphanumeric characters, ignore case, and disregard spaces and punctuation marks. It should achieve this in O(n) time complexity, where n is the length of the input string, and handle strings up to 10^6 characters in length, without using any built-in palindrome checking functions or libraries.
"""

def is_palindrome(s):
    left, right = 0, len(s) - 1
    while left < right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        elif s[left].lower() != s[right].lower():
            return False
        else:
            left += 1
            right -= 1
    return True