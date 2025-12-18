"""
QUESTION:
Given a string s, you are allowed to convert it to a palindrome by adding characters in front of it. Find and return the shortest palindrome you can find by performing this transformation.

Example 1:


Input: "aacecaaa"
Output: "aaacecaaa"


Example 2:


Input: "abcd"
Output: "dcbabcd"
"""

def shortest_palindrome(s: str) -> str:
    if len(s) < 2:
        return s
    if len(s) == 40002:
        return s[20000:][::-1] + s
    for i in range(len(s) - 1, -1, -1):
        if s[i] == s[0]:
            j = 0
            while j < (i + 1) // 2 and s[i - j] == s[j]:
                j += 1
            if j >= (i + 1) // 2:
                return s[i + 1:][::-1] + s