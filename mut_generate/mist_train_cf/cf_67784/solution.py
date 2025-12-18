"""
QUESTION:
Given a string `S` and an integer `L`, write a function `countSubstrings(S, L)` that returns the number of substrings that have only one distinct letter and are of length `L`. The input string `S` will consist of only lowercase English letters and will be of length between 1 and 1000, and `L` will be between 1 and the length of `S`.
"""

def countSubstrings(s, L):
    n, res = len(s), 0
    recordList = []
    j = 0

    for i in range(n):
        if i == n-1 or s[i] != s[i+1]:
            recordList.append(i - j + 1)
            j = i + 1

    for i in range(len(recordList)):
        if recordList[i] >= L:
            res += recordList[i] - L + 1
            
    return res