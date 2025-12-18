"""
QUESTION:
Write a function named `is_palindrome` that takes a string `s` as input and returns a boolean value indicating whether the string is a palindrome. The function should convert the input string to lowercase, ignore any case sensitivity, and not use any built-in string reversal or palindrome-checking functions.
"""

def is_palindrome(s):
    # convert input string to lowercase
    s = s.lower()
    
    # initialize left and right pointers
    left = 0
    right = len(s) - 1
    
    # iterate through the string from both ends
    while left < right:
        # check if characters at left and right positions are equal
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True