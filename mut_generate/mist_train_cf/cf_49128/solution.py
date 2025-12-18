"""
QUESTION:
Create a function `is_palindrome` that determines whether a given string constitutes a palindrome or not, considering only alphanumeric characters and ignoring cases, with a time complexity of O(n) and space complexity of O(1). The function should take a string as input and return a boolean value indicating whether the string is a palindrome or not.
"""

import re

def is_palindrome(input_string):
    input_string = re.sub('\W+','', input_string.lower())
    left = 0
    right = len(input_string) - 1
    
    while left < right:
        if input_string[left] != input_string[right]:
            return False
        left += 1
        right -= 1
    return True