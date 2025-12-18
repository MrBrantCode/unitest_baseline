"""
QUESTION:
Check if it's possible to construct a palindrome by concatenating segments of two given strings `a` and `b` of identical length.

Write a function `checkPalindromeFormation(a: str, b: str) -> bool` that returns `true` if a palindrome can be formed, and `false` otherwise. 

Restrictions: 
- `1 <= a.length, b.length <= 10^5`
- `a.length == b.length`
- `a` and `b` are composed of lowercase English alphabets.
"""

def checkPalindromeFormation(a: str, b: str) -> bool:
    def check(s1: str, s2: str) -> bool:
        i, j = 0, len(s1) - 1
        while i < j and s1[i] == s2[j]:
            i += 1
            j -= 1
        s = s1[i:j+1]
        return s == s[::-1]
    
    return check(a, b) or check(b, a)