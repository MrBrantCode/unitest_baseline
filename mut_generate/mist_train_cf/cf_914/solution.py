"""
QUESTION:
Write a function named `is_palindrome` that takes a string `s` as input and returns a boolean value indicating whether the string is a palindrome, ignoring non-alphanumeric characters and treating uppercase and lowercase letters as equivalent. The function should have a time complexity of O(n) and not use any built-in library or function for reversing the string.
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