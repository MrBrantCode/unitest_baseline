"""
QUESTION:
Mike has a string s consisting of only lowercase English letters. He wants to change exactly one character from the string so that the resulting one is a palindrome. 

A palindrome is a string that reads the same backward as forward, for example strings "z", "aaa", "aba", "abccba" are palindromes, but strings "codeforces", "reality", "ab" are not.

Input

The first and single line contains string s (1 ≤ |s| ≤ 15).

Output

Print "YES" (without quotes) if Mike can change exactly one character so that the resulting string is palindrome or "NO" (without quotes) otherwise. 

Examples

Input

abccaa


Output

YES


Input

abbcca


Output

NO


Input

abcda


Output

YES
"""

def can_become_palindrome_with_one_change(s: str) -> str:
    t = 0
    for i in range(len(s) // 2):
        if s[i] != s[-i - 1]:
            t += 1
    
    if (len(s) % 2 == 1 and t < 2) or (len(s) % 2 == 0 and t == 1):
        return 'YES'
    else:
        return 'NO'