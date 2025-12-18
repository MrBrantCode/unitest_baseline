"""
QUESTION:
Create a function `get_longest_palindrome_length` that takes a string as input and returns the length of the longest palindrome substring. The function should ignore non-alphanumeric characters, be case-insensitive, and have a time complexity of O(n^2) and a space complexity of O(1). The input string can contain up to 1 million characters and may include Unicode characters.
"""

def get_longest_palindrome_length(s):
    s = ''.join(filter(str.isalnum, s)).lower()
    n = len(s)
    if n < 2:
        return n

    max_length = 0
    for i in range(n):
        length = _expand_around_center(s, i, i)
        max_length = max(max_length, length)
        
        if i < n - 1 and s[i] == s[i+1]:
            length = _expand_around_center(s, i, i+1)
            max_length = max(max_length, length)
    
    return max_length

def _expand_around_center(s, left, right):
    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1
    return right - left - 1