"""
QUESTION:
Implement the function `insertion_sort(arr)` that sorts the elements of the input array `arr` in non-decreasing order. The array `arr` may contain duplicate elements and at most 10^9 elements, with each element being a float between -10^9 and 10^9 (inclusive). The function should have a time complexity of O(n^2) and should not use any built-in sorting functions or libraries. Additionally, the function should be able to handle large arrays that cannot fit into memory by reading and sorting the array in chunks, using external memory or disk storage if necessary, and then merging the sorted chunks to produce the final sorted array.
"""

import math

def insertion_sort(arr):
    if len(arr) <= 1:
        return arr

    chunk_size = int(math.sqrt(len(arr)))
    chunks = [arr[i:i+chunk_size] for i in range(0, len(arr), chunk_size)]

    for chunk in chunks:
        for i in range(1, len(chunk)):
            key = chunk[i]
            j = i - 1
            while j >= 0 and chunk[j] > key:
                chunk[j + 1] = chunk[j]
                j -= 1
            chunk[j + 1] = key

    sorted_arr = []
    while chunks:
        smallest = float('inf')
        smallest_chunk = None
        for chunk in chunks:
            if chunk[0] <= smallest:
                smallest = chunk[0]
                smallest_chunk = chunk
        sorted_arr.append(smallest)
        smallest_chunk.pop(0)
        if len(smallest_chunk) == 0:
            chunks.remove(smallest_chunk)

    return sorted_arr