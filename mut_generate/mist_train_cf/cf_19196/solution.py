"""
QUESTION:
Implement a function `longest_palindrome(s)` that takes a string `s` as input and returns the longest palindromic substring in `s`. The function should handle both odd and even-length palindromic substrings and return the first one encountered in case of a tie.
"""

def longest_palindrome(s):
    if not s:
        return ""
    
    start = 0
    end = 0
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    for i in range(len(s)):
        len1 = expand_around_center(i, i)  
        len2 = expand_around_center(i, i + 1)  
        length = max(len1, len2)
        
        if length > end - start:
            start = i - (length - 1) // 2
            end = i + length // 2
    
    return s[start:end+1]