"""
QUESTION:
Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.
"""

def find_longest_substring_length(s: str) -> int:
    L, res, last = -1, 0, {}
    for R, char in enumerate(s):
        if char in last and last[char] > L:
            L = last[char]
        elif R - L > res:
            res = R - L
        last[char] = R
    return res