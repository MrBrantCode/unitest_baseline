"""
QUESTION:
Create a function `is_palindrome` that takes a string as input and returns `True` if the string is a palindrome (i.e., reads the same backward as forward) and `False` otherwise. The function should handle the input string as case-sensitive and without any whitespace or punctuation removal.
"""

def is_palindrome(s):
    # reverse the string 
    rev_str = s[::-1] 
  
    # if string is equal then return true 
    return rev_str == s