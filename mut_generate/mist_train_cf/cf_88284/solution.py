"""
QUESTION:
Write a function `is_palindrome(string)` that checks if a given string is a palindrome, ignoring non-alphabetic characters and considering the string case-insensitive. The function should have a time complexity of O(n) and use constant space.
"""

def is_palindrome(string):
    start = 0
    end = len(string) - 1
    
    while start < end:
        if not string[start].isalpha():
            start += 1
            continue
        
        if not string[end].isalpha():
            end -= 1
            continue
        
        if string[start].lower() != string[end].lower():
            return False
        
        start += 1
        end -= 1
    
    return True