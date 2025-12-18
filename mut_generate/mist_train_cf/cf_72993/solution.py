"""
QUESTION:
Given a string `text` of length `n` where `3 <= n <= 20000`, and `text` consists of lowercase English characters only, find the length of the longest substring with repeated characters after swapping two non-adjacent characters in the string. Implement a function `maxRepOpt1` that takes `text` as input and returns the length of the longest repeated character substring.
"""

def maxRepOpt1(text: str) -> int:
    cnt, maxf, n = [0]*26, [0]*26, len(text)
    A = [ord(text[i]) - ord('a') for i in range(n)]
    res = maxf[A[0]] = 1
    for i in range(1, n):
        if A[i-1] == A[i]:
            cur = cnt[A[i-1]] + 2
            if cnt[A[i-1]] < maxf[A[i-1]]:
                cur -= 1
            res = max(res, cur)
            cnt[A[i-1]] = 0
        else:
            cnt[A[i-1]] = maxf[A[i-1]]
            res = max(res, maxf[A[i]] + 1)
        maxf[A[i]] = max(maxf[A[i]], cnt[A[i]] + 1)
    return res