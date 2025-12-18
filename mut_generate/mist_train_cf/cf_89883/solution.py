"""
QUESTION:
Write a function `is_palindrome` that determines if a given string is a palindrome, ignoring case, spaces, and punctuation. The function should return True if the string is a palindrome and False otherwise. The solution must not use any built-in string manipulation or regular expression functions.
"""

def is_palindrome(s):
    # Remove punctuation marks, spaces, and convert to lowercase
    alphanumeric_string = ''.join(char.lower() for char in s if char.isalnum())
    
    # Use two pointers to compare characters from both ends
    left, right = 0, len(alphanumeric_string) - 1
    while left < right:
        if alphanumeric_string[left] != alphanumeric_string[right]:
            return False
        left += 1
        right -= 1
    
    return True