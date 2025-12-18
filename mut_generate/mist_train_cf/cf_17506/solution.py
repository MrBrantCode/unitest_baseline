"""
QUESTION:
Implement a function `is_palindrome(s)` that determines if the input string `s` is a palindrome. A palindrome is a string that reads the same forwards and backwards. The function should ignore non-alphanumeric characters, spaces, and case. The input string `s` consists of lowercase and/or uppercase letters, spaces, and/or punctuation marks, and its length is between 1 and 10^5. The function should return `True` if `s` is a palindrome and `False` otherwise.
"""

def entrance(s: str) -> bool:
    s = s.lower()
    i = 0
    j = len(s) - 1
    
    while i < j:
        if not s[i].isalnum():
            i += 1
        elif not s[j].isalnum():
            j -= 1
        elif s[i] != s[j]:
            return False
        else:
            i += 1
            j -= 1
    
    return True