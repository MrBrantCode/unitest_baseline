"""
QUESTION:
Create a function called `isPalindrome` that takes a string `s` as its parameter and returns `True` if the string is a palindrome (ignoring special characters and considering case sensitivity) and `False` otherwise. The function should have a time complexity of O(n) for both time and space, not O(log n), since the string must be scanned at least once to check for palindromes and special characters are filtered.
"""

def isPalindrome(s):
    normalizedStr = ''.join(ch for ch in s if ch.isalnum())
    start = 0
    end = len(normalizedStr) - 1
    
    while start < end:
        if normalizedStr[start] != normalizedStr[end]:
            return False
        start += 1
        end -= 1
    
    return True