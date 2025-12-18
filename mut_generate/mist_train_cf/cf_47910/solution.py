"""
QUESTION:
Develop a Python function `longestStringInRange` that accepts an array of textual elements `text_arr` and two numeric parameters `k1` and `k2`. Return the longest text in `text_arr` whose number of characters is within the range of `k1` and `k2` (inclusive). The function should be optimized for large inputs and handle edge cases. The size of `text_arr` can be as large as 10^5 and the lengths of the strings range from 1 to 1000.
"""

import heapq

def longestStringInRange(text_arr, k1, k2):
    if not text_arr or k1 > k2 or k1 < 0 or k2 < 0:
        return None  # handle edge cases of invalid input
    
    # Use a heap to keep least very lengthy texts as of now
    heap = [(-len(s), s) for s in text_arr if k1 <= len(s) <= k2]
    heapq.heapify(heap)

    if not heap:
        return None  # if no string fall into the range of k1 to k2

    return heapq.heappop(heap)[1]  # return the textual element with most length