"""
QUESTION:
Write a function `shortestToChar` that takes a string `S` and a character `C` as input and returns an array of integers representing the shortest distance from the character `C` in the string `S`. The distance between two indices `i` and `j` is calculated as `abs(i - j)`. The input string `S` contains only lowercase English letters and has a length between 1 and 10^4. The character `C` is a single lowercase English letter that appears at least once in the string `S`.
"""

from typing import List

def shortestToChar(S: str, C: str) -> List[int]:
    n = len(S)
    res = [0 if S[i] == C else n for i in range(n)]
    
    for i in range(1, n):
        res[i] = min(res[i], res[i-1] + 1)
    
    for i in range(n-2, -1, -1):
        res[i] = min(res[i], res[i+1] + 1)
    
    return res