"""
QUESTION:
Write a function `kth_highest_freq(s, k)` that takes a string `s` and an integer `k` as input and returns the character that represents the `k`th highest frequency within the string `s`. The function should assume `k` is valid (i.e., `k > 0` and `k` is not greater than the total number of distinct characters in `s`) and should not count spaces.
"""

import collections
import heapq

def kth_highest_freq(s, k):
    char_counter = collections.Counter(c for c in s if c != ' ')
    
    freq_heap = []
    for char, freq in char_counter.items():
        if len(freq_heap) < k:
            heapq.heappush(freq_heap, (freq, char))
        else:
            if freq > freq_heap[0][0]:
                heapq.heapreplace(freq_heap, (freq, char))

    return freq_heap[0][1] if freq_heap else None