"""
QUESTION:
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true


Example 2:


Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false
"""

def is_interleaved(s1: str, s2: str, s3: str) -> bool:
    if len(s3) != len(s1) + len(s2):
        return False
    if not s1 or not s2:
        return (s1 or s2) == s3
    options = {(0, 0)}
    for char in s3:
        new_options = set()
        for (i1, i2) in options:
            if i1 < len(s1) and char == s1[i1]:
                new_options.add((i1 + 1, i2))
            if i2 < len(s2) and char == s2[i2]:
                new_options.add((i1, i2 + 1))
        options = new_options
        if not options:
            return False
    return True