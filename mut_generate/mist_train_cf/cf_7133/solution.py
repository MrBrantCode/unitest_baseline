"""
QUESTION:
Write a Python function `longest_palindrome_odd_distinct` that takes a string `s` as input and returns the length of the longest palindromic substring that contains an odd number of distinct characters. The function should have a time complexity of O(n^2), where n is the length of the input string `s`. The input string `s` can contain both uppercase and lowercase letters, special characters, numbers, and can be an empty string.
"""

def longest_palindrome_odd_distinct(s):
    n = len(s)
    max_len = 0

    for i in range(n):
        # Expand from center for odd-length palindromes
        left = i
        right = i
        distinct_chars = set()
        
        while left >= 0 and right < n:
            distinct_chars.add(s[left])
            if s[left] != s[right]:
                break
            if len(distinct_chars) % 2 == 1:
                max_len = max(max_len, right - left + 1)
            left -= 1
            right += 1

        # Expand from center for even-length palindromes
        left = i
        right = i + 1
        distinct_chars = set()
        
        while left >= 0 and right < n:
            distinct_chars.add(s[left])
            if s[left] != s[right]:
                break
            if len(distinct_chars) % 2 == 1:
                max_len = max(max_len, right - left + 1)
            left -= 1
            right += 1

    return max_len