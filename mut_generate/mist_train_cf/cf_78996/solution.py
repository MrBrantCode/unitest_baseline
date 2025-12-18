"""
QUESTION:
Create a Huffman Tree from a specified collection of symbols with their corresponding frequencies. 

The function should be named `build_huffman_tree` and it should take a dictionary of symbols and their frequencies as input. The output should be a dictionary where the keys are the symbols and the values are their corresponding Huffman codes. 

Assume that the input dictionary will always contain at least two symbols and the frequencies will be positive integers. The output Huffman codes should be strings of binary digits. 

Note that there can be multiple correct answers, depending on the order in which nodes are combined.
"""

import heapq
from collections import defaultdict

def build_huffman_tree(frequency):
    heap = [[weight, [symbol, ""]] for symbol, weight in frequency.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        for pair in lo[1:]:
            pair[1] = '0' + pair[1]
        for pair in hi[1:]:
            pair[1] = '1' + pair[1]
        heapq.heappush(heap, [lo[0] + hi[0]] + lo[1:] + hi[1:])
    return sorted(heap[0][1:], key=lambda p: (len(p[-1]), p))

def huffman_code(frequency):
    huffman_tree = build_huffman_tree(frequency)
    huffman_dict = {}
    for p in huffman_tree:
        huffman_dict[p[0]] = p[1]
    return huffman_dict