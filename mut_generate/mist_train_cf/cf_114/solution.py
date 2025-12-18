"""
QUESTION:
Write a function `is_palindrome` that checks if a given string is a palindrome, ignoring case. The function should have a time complexity of O(n) and a space complexity of O(1), and it should not use any built-in string reversal functions or data structures.
"""

def is_palindrome(s):
    start = 0
    end = len(s) - 1

    while start < end:
        if s[start].lower() != s[end].lower():
            return False
        start += 1
        end -= 1

    return True