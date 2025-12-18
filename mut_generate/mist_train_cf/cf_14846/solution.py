"""
QUESTION:
Write a function `longestPalindrome(s)` that finds the longest palindromic substring of a given input string `s` with a length of at most 10^5. The function should have a time complexity of O(n) and should not use any extra space other than a constant amount of additional memory.
"""

def longestPalindrome(s):
    if len(s) < 2:
        return s
    
    start = 0
    maxLength = 0
    
    for center in range(1, len(s) - 1):
        left = right = center
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        length = right - left - 1
        
        if length > maxLength:
            maxLength = length
            start = left + 1
            
    for center in range(len(s)):
        left = right = center
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        length = right - left - 1
        
        if length > maxLength:
            maxLength = length
            start = left + 1
    
    for center in range(len(s) - 1):
        left = center
        right = center + 1
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        
        length = right - left - 1
        
        if length > maxLength:
            maxLength = length
            start = left + 1
            
    return s[start:start + maxLength]