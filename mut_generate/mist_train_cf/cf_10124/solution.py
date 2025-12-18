"""
QUESTION:
Write a function called `is_palindrome` that checks if a given string is a palindrome. The string is considered a palindrome if it reads the same backward as forward, ignoring non-alphabetic characters and letter case. The function should return True if the string is a palindrome and False otherwise. The input string should not exceed 100 characters and should only contain alphabetic characters.
"""

def is_palindrome(s):
    # Remove non-alphabetic characters and convert to lowercase
    s = ''.join(filter(str.isalpha, s.lower()))
    
    # Check if the string is equal to its reverse
    return s == s[::-1]