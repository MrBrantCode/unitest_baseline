"""
QUESTION:
Write a function `rearrangeBarcodes(barcodes)` to reorganize a sequence of barcodes such that no two consecutive barcodes are identical. The function takes a list of integers `barcodes` where `1 <= barcodes.length <= 10000` and `1 <= barcodes[i] <= 10000` as input and returns the reorganized list of barcodes.
"""

import collections, heapq
def rearrangeBarcodes(barcodes):
    freq_dic = collections.Counter(barcodes)
    max_heap = []
    for key, values in freq_dic.items():
        heapq.heappush(max_heap, (-values, key))
    result = []
    while len(max_heap) > 1:
        v1, k1 = heapq.heappop(max_heap)
        v2, k2 = heapq.heappop(max_heap)
        result.extend([k1, k2])
        if v1 < -1:
            heapq.heappush(max_heap, (v1+1, k1))
        if v2 < -1:
            heapq.heappush(max_heap, (v2+1, k2))
    if max_heap:
        result.append(max_heap[0][1])
    return result