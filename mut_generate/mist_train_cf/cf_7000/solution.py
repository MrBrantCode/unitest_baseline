"""
QUESTION:
Write a function `kthMostFrequentChar(s, k)` that finds the kth most frequent character in a given string `s`. The function should take a string `s` and an integer `k` as input, and return the kth most frequent character in `s`. The string `s` only contains ASCII characters, and `k` is within the range of 1 to the number of unique characters in `s`. The length of `s` is at most 10^6.
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