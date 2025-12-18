"""
QUESTION:
Rearrange the characters of a given string in the order of their frequency, while ensuring that no two adjacent characters are the same.

Function signature: `def rearrange_string(string: str) -> str:`

Input:
- A string `string` consisting of lowercase English letters. (1 ≤ len(string) ≤ 10^5)

Output:
- Return a string representing the rearranged characters of the given string.

Restriction: 
- The characters with the highest frequency come first, followed by characters with lower frequencies.
- No two adjacent characters are the same.
"""

from collections import Counter
import heapq

def rearrange_string(string: str) -> str:
    freq = Counter(string)
    max_heap = [(-count, char) for char, count in freq.items()]
    heapq.heapify(max_heap)
    result = ''
    prev_char = None
    prev_count = 0
    
    while max_heap:
        count, char = heapq.heappop(max_heap)
        result += char
        
        if prev_count < 0:
            heapq.heappush(max_heap, (prev_count, prev_char))
        
        prev_char = char
        prev_count = count + 1
    
    if len(result) == len(string):
        return result
    else:
        return ''