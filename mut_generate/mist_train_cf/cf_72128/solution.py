"""
QUESTION:
Implement the function `shortestPalindrome(s)` that transforms a given string `s` into a palindrome by appending characters to its beginning. The goal is to determine the shortest possible palindrome that can be achieved through this transformation process. The string `s` contains only lowercase English alphabets and its length is within the range `0 <= s.length <= 5 * 10^4`.
"""

def shortestPalindrome(s):
    n = len(s)
    rev_s = s[::-1]
    for i in range(n):
        if s.startswith(rev_s[i:]):
            return rev_s[:i] + s
    return ''