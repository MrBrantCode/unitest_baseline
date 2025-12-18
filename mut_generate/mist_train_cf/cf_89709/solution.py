"""
QUESTION:
Write a function `kthMostFrequentChar(s, k)` that takes a string `s` and an integer `k` as input, and returns the kth most frequent character in `s`. The string `s` only contains ASCII characters and has a maximum length of 10^6. The value of `k` is between 1 and the number of unique characters in `s`.
"""

def kthMostFrequentChar(s, k):
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    sorted_freq = sorted(freq.items(), key=lambda x: x[1], reverse=True)
    
    return sorted_freq[k-1][0]