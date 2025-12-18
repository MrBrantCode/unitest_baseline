"""
QUESTION:
Given a string s, partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:


Input: "aab"
Output: 1
Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.
"""

def min_palindrome_cuts(s: str) -> int:
    if s == s[::-1]:
        return 0
    if any((s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1] for i in range(1, len(s)))):
        return 1
    cut = [x for x in range(-1, len(s))]
    for i in range(len(s)):
        (r1, r2) = (0, 0)
        while r1 <= i < len(s) - r1 and s[i - r1] == s[i + r1]:
            (cut[i + r1 + 1], r1) = (min(cut[i + r1 + 1], cut[i - r1] + 1), r1 + 1)
        while r2 <= i < len(s) - r2 - 1 and s[i - r2] == s[i + r2 + 1]:
            (cut[i + r2 + 2], r2) = (min(cut[i + r2 + 2], cut[i - r2] + 1), r2 + 1)
    return cut[-1]