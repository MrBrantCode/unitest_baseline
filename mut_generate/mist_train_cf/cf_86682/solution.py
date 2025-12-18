"""
QUESTION:
Write a function `is_palindrome(s)` that determines if a given string `s` is a palindrome. The function should disregard non-alphanumeric characters, treat uppercase and lowercase letters as equivalent, and handle Unicode characters. It must achieve this in a time complexity of O(n) without using built-in string reversal functions.
"""

def is_palindrome(s):
    # Initialize two pointers at the start and end of the string
    i, j = 0, len(s) - 1
    
    while i < j:
        # Increment the left pointer if the character at that position is not alphanumeric
        while i < j and not s[i].isalnum():
            i += 1
        # Decrement the right pointer if the character at that position is not alphanumeric
        while i < j and not s[j].isalnum():
            j -= 1
        
        # Compare the lowercase characters at the current pointers
        if s[i].lower() != s[j].lower():
            return False
        
        # Move the pointers closer to the center
        i += 1
        j -= 1
    
    return True