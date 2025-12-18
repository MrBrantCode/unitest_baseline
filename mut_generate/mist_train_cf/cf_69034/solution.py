"""
QUESTION:
Given a string `s` and an integer `k`, write a function `rearrange(s, k)` that rearranges `s` such that identical characters are separated by a minimum distance of `k` from each other. If the string cannot be rearranged to meet this condition, return an empty string. 

The length of `s` is between 1 and 3 * 10^5 and `s` is composed solely of lowercase English alphabets. The value of `k` is between 0 and the length of `s`.
"""

import collections
import heapq

def rearrange_string(s, k):
    if k == 0:
        return s
    counter = collections.Counter(s)
    heap = []
    for key, freq in counter.items():
        heapq.heappush(heap, (-freq, key))
    res = []
    queue = collections.deque()
    while heap:
        freq, char = heapq.heappop(heap)
        res.append(char)
        queue.append((freq + 1, char))
        if len(queue) < k:
            continue
        freq, char = queue.popleft()
        if freq < 0:
            heapq.heappush(heap, (freq, char))
    return ''.join(res) if len(res) == len(s) else ''