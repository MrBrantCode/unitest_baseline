"""
QUESTION:
Write a function `is_palindrome(input_string)` that checks if an input string is a palindrome. The function should ignore non-alphabetic characters, be case-insensitive, and not use any built-in string reversal or palindrome-checking functions. It should return `True` if the input string is a palindrome and `False` otherwise.
"""

def is_palindrome(input_string):
    # Remove special characters, numbers, and spaces from the input string
    cleaned_string = ''.join(char.lower() for char in input_string if char.isalpha())
    
    # Initialize two pointers at the start and end of the string
    left = 0
    right = len(cleaned_string) - 1
    
    # Compare characters at the left and right pointers
    while left < right:
        if cleaned_string[left] != cleaned_string[right]:
            return False
        left += 1
        right -= 1
    
    # If the loop completes without finding a mismatch, the string is a palindrome
    return True