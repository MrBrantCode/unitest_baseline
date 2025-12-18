"""
QUESTION:
Create a function `rearrange_string` that takes a string `my_str` as input. The function should rearrange the characters in `my_str` such that no two consecutive characters are the same. If a solution exists, the function should return the length of the longest possible subsequence of characters in the rearranged string without any repeats. If it is not possible to rearrange the string, the function should return -1.
"""

import heapq
from collections import Counter

def rearrange_string(my_str):
    char_count_map = Counter(my_str)  

    max_heap = []
    for char, count in char_count_map.items():  
        max_heap.append((-count, char))  

    heapq.heapify(max_heap)

    prev_char, prev_count = '', 0
    result = ''
    while max_heap:  
        count, char = heapq.heappop(max_heap)
        result += char
        if prev_count < 0:  
            heapq.heappush(max_heap, (prev_count, prev_char))
        count += 1
        prev_char, prev_count = char, count  

    if len(result) == len(my_str):
        return len(result)
    else:
        return -1  