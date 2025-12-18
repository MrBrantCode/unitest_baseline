"""
QUESTION:
Implement the function `rearrange_string(my_str: str) -> str` to rearrange the characters in the input string such that no two consecutive characters are the same, and the rearranged string is the lexicographically smallest possible among all valid rearrangements. Assume the input string contains only lowercase English letters and has at least one valid rearrangement.
"""

from typing import Dict
from heapq import heappop, heappush

def rearrange_string(my_str: str) -> str:
    freq_count = {}
    for char in my_str:
        freq_count[char] = freq_count.get(char, 0) + 1
    
    pq = [(freq, char) for char, freq in freq_count.items()]
    heapify(pq)

    rearranged_str = ""
    while pq:
        freq1, char1 = heappop(pq)
        if rearranged_str and rearranged_str[-1] == char1:
            if not pq:
                return ""  # No valid rearrangement is possible
            freq2, char2 = heappop(pq)
            rearranged_str += char2
            freq2 -= 1
            if freq2 > 0:
                heappush(pq, (freq2, char2))
        rearranged_str += char1
        freq1 -= 1
        if freq1 > 0:
            heappush(pq, (freq1, char1))

    return rearranged_str