"""
QUESTION:
Write a function get_longest_palindrome_length that takes a string as input, strips all whitespace, ignores any non-alphanumeric characters, and returns the length of the longest palindrome substring found in a case-insensitive manner. The function should handle inputs with special characters, whitespace, and Unicode characters, and should have a time complexity of O(n^2) and a space complexity of O(1).
"""

def get_longest_palindrome_length(string):
    string = _sanitize_string(string)
    n = len(string)
    if n < 2:
        return n
    
    max_length = 0
    for i in range(n):
        length = _expand_around_center(string, i, i)
        max_length = max(max_length, length)
        
        if i < n - 1 and string[i] == string[i+1]:
            length = _expand_around_center(string, i, i+1)
            max_length = max(max_length, length)
    
    return max_length

def _sanitize_string(string):
    string = string.lower()
    string = ''.join(filter(str.isalnum, string))
    return string

def _expand_around_center(string, left, right):
    while left >= 0 and right < len(string) and string[left] == string[right]:
        left -= 1
        right += 1
    return right - left - 1