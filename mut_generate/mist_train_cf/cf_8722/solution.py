"""
QUESTION:
Write a function `longest_palindromic_substring(s)` to find the longest palindromic substring in a given string `s`. The input string can contain any printable ASCII characters and its length can be up to 10^6 characters. The function should return the longest palindromic substring found in the input string.
"""

def longest_palindromic_substring(s):
    if len(s) < 2:
        return s
    
    start = 0
    max_len = 1
    
    for i in range(len(s)):
        # check odd length palindromes
        left = i - 1
        right = i + 1
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1
        
        # check even length palindromes
        left = i
        right = i + 1
        
        while left >= 0 and right < len(s) and s[left] == s[right]:
            if right - left + 1 > max_len:
                start = left
                max_len = right - left + 1
            left -= 1
            right += 1
    
    return s[start:start + max_len]