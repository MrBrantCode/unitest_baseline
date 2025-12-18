"""
QUESTION:
Create a function named `is_palindrome` that takes two strings as input. The function should determine if the first string is a palindrome of the second string, considering all characters including spaces, punctuation, and capitalization. The function should handle strings up to a maximum length of 1 million characters and optimize its performance to minimize memory usage.
"""

def is_palindrome(s1, s2):
    s1 = ''.join(filter(str.isalnum, s1)).lower()
    s2 = ''.join(filter(str.isalnum, s2)).lower()
    
    length = len(s1)
    if length != len(s2):
        return False
    
    for i in range(length):
        if s1[i] != s2[length - i - 1]:
            return False
    
    return True