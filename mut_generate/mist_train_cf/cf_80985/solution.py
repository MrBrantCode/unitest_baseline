"""
QUESTION:
Given a string `s` of length between 1 and 2000, consisting of lowercase and/or uppercase English letters, write a function `longestPalindrome(s)` that returns the length of the longest palindrome that can be built with those letters, with the restriction that the palindrome must have a unique center (i.e., no double letters at the center).
"""

import collections

def longestPalindrome(s):
    count = collections.Counter(s) 
    length = 0
    for v in count.values():
        length += v // 2 * 2
        if length % 2 == 0 and v % 2 == 1:
            length += 1
    return length