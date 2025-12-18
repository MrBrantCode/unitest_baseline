"""
QUESTION:
Given a string s, define a function uniqueLetterString(s) that calculates the cumulative sum of unique characters in all substrings of s, where each unique character in a substring contributes to the sum. The function should return the result modulo 10^9 + 7. The input string s consists of only uppercase English letters and its length is between 0 and 10^4.
"""

def uniqueLetterString(s):
    index = [[-1, -1] for _ in range(26)]
    res = 0
    mod = 10 ** 9 + 7
    N = len(s)
    
    for i in range(N):
        c = ord(s[i]) - ord('A')
        res = (res + (i - index[c][1]) * (index[c][1] - index[c][0]) % mod) % mod
        index[c] = [index[c][1], i]
        
    for c in range(26):
        res = (res + (N - index[c][1]) * (index[c][1] - index[c][0]) % mod) % mod
    
    return res