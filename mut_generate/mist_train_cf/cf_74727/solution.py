"""
QUESTION:
Given an alphanumeric string `S` and an integer `K`, return the count of substrings that are of length `K` and do not contain any recurring characters. The length of `S` is at least 1 and at most 10^4, all characters in `S` are lowercase English alphabets, and the value of `K` is at least 1 and at most 10^4.
"""

def entrance(s, k):
    if len(s) < k:
        return 0
    freq = [0] * 26
    result = 0
    start = 0
    for end in range(len(s)):
        freq[ord(s[end]) - ord('a')] += 1
        if end - start + 1 == k:
            if max(freq) == 1:
                result += 1
            freq[ord(s[start]) - ord('a')] -= 1
            start +=1
    return result