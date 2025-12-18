"""
QUESTION:
Given a list of lowercase words and an integer k, return the k most frequent words in descending order of frequency. If two words share the same frequency, prioritize the word that comes first in alphabetical order. Assume that k is always valid, ranging from 1 to the total number of unique elements.
"""

import collections
import heapq
from typing import List

def topKFrequent(words: List[str], k: int) -> List[str]:
    count = collections.Counter(words)
    heap = [(-freq, word) for word, freq in count.items()]
    heapq.heapify(heap)
    return [heapq.heappop(heap)[1] for _ in range(k)]