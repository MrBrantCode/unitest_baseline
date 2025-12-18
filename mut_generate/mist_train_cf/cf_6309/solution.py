"""
QUESTION:
Create a function called `is_palindrome` that takes a string `s` as input and returns a boolean value indicating whether the string is a palindrome, ignoring spaces, punctuation, and capitalization, and only considering alphanumeric characters. The function should have a time complexity of O(n) and a space complexity of O(1), where n is the length of the input string.
"""

import re

def is_palindrome(s):
    # Remove non-alphanumeric characters and convert to lowercase
    s = re.sub('[^a-zA-Z0-9]', '', s).lower()
    
    start, end = 0, len(s) - 1
    
    while start <= end:
        if s[start] != s[end]:
            return False
        start += 1
        end -= 1
    
    return True