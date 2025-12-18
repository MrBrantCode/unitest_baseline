"""
QUESTION:
Create a function named `is_palindrome` that takes two strings as arguments. The function should determine if the second string is a palindrome of the first string, ignoring spaces, punctuation, and capitalization. The function should return a boolean value indicating whether the second string is a palindrome of the first string.
"""

def is_palindrome(s1, s2):
    # Remove spaces, punctuation, and convert to lowercase
    s1 = "".join(s1.lower().split())
    s2 = "".join(s2.lower().split())
    
    # Check if the reversed string is equal to the original string
    return s1 == s2[::-1]