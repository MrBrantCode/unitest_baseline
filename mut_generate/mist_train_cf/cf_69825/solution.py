"""
QUESTION:
Create a function called `is_palindrome` that accepts a string as input and returns a boolean value indicating whether the string is a palindrome, i.e., reads the same backward as forward. The function should perform a case-sensitive comparison and include all characters in the input string.
"""

def entrance(s):
    # The function uses slicing to reverse the string then checks if it's equal to its original form.
    # The reverse string is acquired by s[::-1] where [::-1] means full slice from end to start.
    return s == s[::-1]