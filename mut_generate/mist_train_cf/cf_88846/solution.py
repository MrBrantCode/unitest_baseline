"""
QUESTION:
Write a function named `is_palindrome` that determines if a given string is a palindrome or not. The function should ignore spaces, punctuation, and capitalization, but consider non-alphabetic characters as part of the palindrome if they are in the original input string. The function should return `True` if the string is a palindrome and `False` otherwise. The solution should have a time complexity of O(n) and a space complexity of O(1).
"""

def is_palindrome(string):
    left = 0
    right = len(string) - 1

    while left < right:
        if not string[left].isalnum():
            left += 1
        elif not string[right].isalnum():
            right -= 1
        elif string[left].lower() != string[right].lower():
            return False
        else:
            left += 1
            right -= 1

    return True