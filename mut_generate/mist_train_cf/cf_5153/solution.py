"""
QUESTION:
Implement a function `is_palindrome` that takes a string as input and returns `True` if the string is a palindrome and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the input string, and should not use any additional space other than the input string. Additionally, it should not use any built-in string manipulation methods or libraries.
"""

def entrance(s):
    n = len(s)
    for i in range(n // 2):
        if s[i] != s[n - 1 - i]:
            return False
    return True