"""
QUESTION:
Write a function called `longest_palindromic_substring` that takes a character sequence `s` as input and returns the longest palindromic substring in `s`. The length of `s` will not exceed 1000 characters.
"""

def longest_palindromic_substring(s):
    if len(s) < 2:
        return s
    
    def expand_around_center(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

    start, end = 0, 0
    for i in range(len(s)):
        # Case 1: odd-length palindromic substring
        l1 = expand_around_center(i, i)
        # Case 2: even-length palindromic substring
        l2 = expand_around_center(i, i + 1)
        length = max(l1, l2)
        
        if length > end - start:
            start = i - (length - 1) // 2
            end = i + length // 2
    
    return s[start:end+1]