"""
QUESTION:
Write a function `minDeletions(s)` that takes a string `s` of lowercase English letters as input and returns the minimum number of characters that need to be deleted to make `s` good, where a string is good if there are no two different characters in `s` that have the same frequency. If there are multiple solutions, the function should return the one that results in the lexicographically smallest string. The length of `s` is between 1 and 10^5.
"""

import collections
import heapq

def minDeletions(s: str) -> int:
    counter = collections.Counter(s)
    frequencies = list(counter.values())
    frequencies = [-freq for freq in frequencies]
    heapq.heapify(frequencies)
    deletions = 0
    while len(frequencies) > 1:
        freq1 = heapq.heappop(frequencies)
        if frequencies[0] == freq1:
            freq1 += 1
            deletions += 1
            if freq1 < 0:
                heapq.heappush(frequencies, freq1)
    return deletions