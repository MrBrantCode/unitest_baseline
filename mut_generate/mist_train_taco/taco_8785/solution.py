"""
QUESTION:
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. In other words, one of the first string's permutations is the substring of the second string.

Example 1:

Input:s1 = "ab" s2 = "eidbaooo"
Output:True
Explanation: s2 contains one permutation of s1 ("ba").



Example 2:

Input:s1= "ab" s2 = "eidboaoo"
Output: False



Note:

The input strings only contain lower case letters.
The length of both given strings is in range [1, 10,000].
"""

def contains_permutation(s1: str, s2: str) -> bool:
    if len(s2) < len(s1):
        return False
    
    c1 = [0] * 128
    n = 0
    
    for char in s1:
        c = ord(char)
        if c1[c] == 0:
            n += 1
        c1[c] += 1
    
    for i in range(len(s1)):
        c = ord(s2[i])
        c1[c] -= 1
        if not c1[c]:
            n -= 1
    
    if not n:
        return True
    
    for i in range(len(s2) - len(s1)):
        c = ord(s2[i])
        if not c1[c]:
            n += 1
        c1[c] += 1
        
        c = ord(s2[i + len(s1)])
        c1[c] -= 1
        if not c1[c]:
            n -= 1
            if not n:
                return True
    
    return False