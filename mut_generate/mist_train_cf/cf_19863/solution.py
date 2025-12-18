"""
QUESTION:
Write a function `is_palindrome(s)` that checks if the input string `s` is a palindrome. The function should have a time complexity of O(n) and not use any additional space other than the input string. It should also not use any built-in string manipulation methods or libraries.
"""

def entrance(s):
    i = 0
    j = len(s) - 1
    
    while i < j:
        if s[i] != s[j]:
            return False
        i += 1
        j -= 1
    
    return True