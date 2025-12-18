"""
QUESTION:
Write a function `is_palindrome` that checks if a given string is a palindrome. The function should use bitwise operations for string manipulation and have a time complexity of O(n) and a space complexity of O(1).
"""

def is_palindrome(str):
    start = 0
    end = len(str) - 1
    
    while start < end:
        # Check if the characters at start and end are different
        if str[start] != str[end]:
            return False
        
        start += 1
        end -= 1
    
    return True