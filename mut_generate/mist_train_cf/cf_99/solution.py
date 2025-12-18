"""
QUESTION:
Function `isPalindrome` checks if a given string is a palindrome. The string may contain uppercase and lowercase letters, numbers, and special characters. The function ignores any spaces or punctuation marks and only considers the alphanumeric characters in the string. It handles strings with a length of up to 10^18 characters and uses a constant amount of additional memory, regardless of the input string length. It also handles different character encodings and multibyte characters, including Unicode characters. The time complexity of the function is O(n), where n is the length of the input string. The function does not use any built-in functions or libraries for checking palindromes.
"""

import unicodedata

def isPalindrome(s):
    left = 0
    right = len(s) - 1

    while left <= right:
        if not s[left].isalnum():
            left += 1
        elif not s[right].isalnum():
            right -= 1
        else:
            if s[left].lower() != s[right].lower():
                return False
            left += 1
            right -= 1
    
    return True