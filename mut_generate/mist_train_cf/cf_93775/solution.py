"""
QUESTION:
Create a function `is_palindrome(string)` that determines if a given string is a palindrome or not. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the string. It should not use any built-in string manipulation functions or data structures.
"""

def is_palindrome(string):
    left = 0
    right = len(string) - 1

    while left <= right:
        if string[left] != string[right]:
            return False
        left += 1
        right -= 1

    return True