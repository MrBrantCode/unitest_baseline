"""
QUESTION:
Write a function named `is_palindrome` that checks if a given input string is a palindrome, ignoring non-alphanumeric characters and being case-insensitive. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

def entance(s):
    s = s.lower()
    start = 0
    end = len(s) - 1
    
    while start < end:
        while not s[start].isalnum():
            start += 1
            if start >= end:
                break
        
        while not s[end].isalnum():
            end -= 1
            if start >= end:
                break
        
        if s[start] != s[end]:
            return False
        
        start += 1
        end -= 1
    
    return True