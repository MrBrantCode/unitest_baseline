"""
QUESTION:
Write a function `aesthetic(s, k)` that calculates and returns the cumulative aesthetic value of all substrings of length `k` within string `s`. The aesthetic value of a string is the difference between the frequency of the most and least occurring characters. Only substrings with entirely unique characters should be considered. The string `s` is composed solely of lowercase English alphabets, and the length of `s` and `k` are within the range of 1 to 500.
"""

def aesthetic(s, k):
    n = len(s)
    cummulative_aesthetic = 0
    
    for i in range(n-k+1):
        substring = s[i:i+k]
        if len(set(substring)) < k: continue
        freq = [substring.count(char) for char in set(substring)]
        cummulative_aesthetic += max(freq) - min(freq)
    
    return cummulative_aesthetic