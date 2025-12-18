"""
QUESTION:
Write a function `is_palindrome(string)` that checks if a given string is a palindrome, ignoring non-alphabetic characters and considering the string case-insensitive. The function should have a time complexity of O(n) and use constant space, without utilizing any built-in functions or libraries for string manipulation. It should also modify the string in-place.
"""

def is_palindrome(s):
    start = 0
    end = len(s) - 1
    
    while start < end:
        if not s[start].isalpha():
            start += 1
            continue
        
        if not s[end].isalpha():
            end -= 1
            continue
        
        if s[start].lower() != s[end].lower():
            return False
        
        start += 1
        end -= 1
    
    return True