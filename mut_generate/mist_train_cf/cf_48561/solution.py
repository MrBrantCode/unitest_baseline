"""
QUESTION:
Write a function `count_substrings(str, k)` that accepts a string `str` and an integer `k` as input. The function should return the count of substrings containing a minimum of `k` distinct characters.
"""

def count_substrings(s, k):
    n = len(s)
    ans = 0
    
    for i in range(k, n + 1):
        for j in range(n - i + 1):
            if len(set(s[j: j + i])) >= k:
                ans += 1
                
    return ans