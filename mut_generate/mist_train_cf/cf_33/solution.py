"""
QUESTION:
Implement a function `is_valid_palindrome(s)` that checks if a given string `s` is a valid palindrome. A valid palindrome is a string that reads the same forwards and backwards, ignoring any non-alphabetic characters and considering only lowercase alphabets. The function should return `True` if the string is a valid palindrome, and `False` otherwise. The function should have a time complexity of O(n), where n is the length of the string.
"""

def is_valid_palindrome(s):
    # Convert the string to lowercase
    s = s.lower()
    
    # Initialize the two pointers
    left = 0
    right = len(s) - 1
    
    while left < right:
        # Check if the left character is not alphabetic
        if not s[left].isalpha():
            left += 1
            continue
        
        # Check if the right character is not alphabetic
        if not s[right].isalpha():
            right -= 1
            continue
        
        # Check if the characters at the two positions are equal
        if s[left] != s[right]:
            return False
        
        # Move the pointers towards the middle
        left += 1
        right -= 1
    
    return True