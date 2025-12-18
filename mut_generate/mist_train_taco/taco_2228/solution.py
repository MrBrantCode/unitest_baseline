"""
QUESTION:
Palindromic characteristics of string s with length |s| is a sequence of |s| integers, where k-th number is the total number of non-empty substrings of s which are k-palindromes.

A string is 1-palindrome if and only if it reads the same backward as forward.

A string is k-palindrome (k > 1) if and only if:   Its left half equals to its right half.  Its left and right halfs are non-empty (k - 1)-palindromes. 

The left half of string t is its prefix of length ⌊|t| / 2⌋, and right half — the suffix of the same length. ⌊|t| / 2⌋ denotes the length of string t divided by 2, rounded down.

Note that each substring is counted as many times as it appears in the string. For example, in the string "aaa" the substring "a" appears 3 times.


-----Input-----

The first line contains the string s (1 ≤ |s| ≤ 5000) consisting of lowercase English letters.


-----Output-----

Print |s| integers — palindromic characteristics of string s.


-----Examples-----
Input
abba

Output
6 1 0 0 

Input
abacaba

Output
12 4 1 0 0 0 0 



-----Note-----

In the first example 1-palindromes are substring «a», «b», «b», «a», «bb», «abba», the substring «bb» is 2-palindrome. There are no 3- and 4-palindromes here.
"""

def calculate_palindromic_characteristics(s: str) -> list[int]:
    n = len(s)
    dp = [[0 for _ in range(n + 1)] for _ in range(n + 1)]
    count = [0 for _ in range(n + 1)]
    
    for sub_len in range(1, n + 1):
        for left in range(0, n - sub_len + 1):
            right = left + sub_len - 1
            if sub_len == 1:
                dp[left][right] = 1
            elif sub_len == 2:
                if s[left] == s[right]:
                    dp[left][right] = 2
            elif s[left] == s[right] and dp[left + 1][right - 1] > 0:
                dp[left][right] = dp[left][left + sub_len // 2 - 1] + 1
            count[dp[left][right]] += 1
    
    for i in range(n - 1, 0, -1):
        count[i] += count[i + 1]
    
    return count[1:]