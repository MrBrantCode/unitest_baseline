"""
QUESTION:
Write a function `longest_palindrome(s)` that identifies the longest palindromic substring in a given string `s`. A palindromic substring is a substring that reads the same forward and backward. If there are multiple palindromic substrings with the same maximum length, return the first one encountered.
"""

def longest_palindrome(s):
    if not s:
        return ""
    
    start = 0
    end = 0
    
    def expand_around_center(s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
            
        return right - left - 1
    
    for i in range(len(s)):
        len1 = expand_around_center(s, i, i)  # Check for odd length palindromes
        len2 = expand_around_center(s, i, i + 1)  # Check for even length palindromes
        length = max(len1, len2)
        
        if length > end - start:
            start = i - (length - 1) // 2
            end = i + length // 2
    
    return s[start:end+1]