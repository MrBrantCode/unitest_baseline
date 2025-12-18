"""
QUESTION:
Write a function named `is_palindrome` that takes a string as input and returns True if the string is a palindrome, and False otherwise. The function should perform a case-insensitive comparison, ignoring any whitespace or punctuation characters. The function should compare characters at corresponding positions in the string, starting from the first and last characters and moving towards the center, and return False as soon as it finds a pair of corresponding characters that are not equal. If no such pair is found, the function should return True.
"""

def is_palindrome(s):
    # Convert the string to lowercase
    s = s.lower()
    
    # Remove whitespace and punctuation characters
    s = ''.join(char for char in s if char.isalnum())
    
    # Compare characters at corresponding positions
    for i in range(len(s)//2):
        if s[i] != s[-i-1]:
            return False
    
    return True