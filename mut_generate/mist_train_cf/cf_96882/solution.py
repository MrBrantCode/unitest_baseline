"""
QUESTION:
Write a function `is_palindrome(str)` that checks if a given string is a palindrome using bitwise operations, with a time complexity of O(n) and a space complexity of O(1). The function should take a string as input and return a boolean value indicating whether the string is a palindrome or not.
"""

def entance(s):
    start = 0
    end = len(s) - 1
    
    while start < end:
        if s[start] != s[end]:
            return False
        
        start += 1
        end -= 1
    
    return True