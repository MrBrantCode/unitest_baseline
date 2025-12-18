"""
QUESTION:
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.


'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).


The matching should cover the entire input string (not partial).

Note:


       s could be empty and contains only lowercase letters a-z.
       p could be empty and contains only lowercase letters a-z, and characters like ? or *.


Example 1:


Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".


Example 2:


Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.


Example 3:


Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.


Example 4:


Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".


Example 5:


Input:
s = "acdcb"
p = "a*c?b"
Output: false
"""

def is_wildcard_match(s: str, p: str) -> bool:
    i = 0
    j = 0
    star = -1
    lenp = len(p)
    while i < len(s):
        if j < lenp and (s[i] == p[j] or p[j] == '?'):
            i += 1
            j += 1
        elif j < lenp and p[j] == '*':
            star = j
            mi = i
            j += 1
        elif star != -1:
            mi += 1
            i = mi
            j = star + 1
        else:
            return False
    while j < lenp and p[j] == '*':
        j += 1
    return j == lenp