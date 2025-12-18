"""
QUESTION:
Implement the function `insertion_sort(arr)` that sorts the elements of the input array `arr` in non-decreasing order using the Insertion Sort algorithm. The array `arr` may contain duplicate elements and should be handled as follows: 
- If the array is small enough to fit into memory, sort the entire array directly. 
- If the array is too large to fit into memory, divide it into chunks of size sqrt(n), sort each chunk in-memory, and then merge the sorted chunks to produce the final sorted array.
The function should have a time complexity of O(n^2) and not use any built-in sorting functions or libraries. The input array may contain at most 10^9 elements, each of which is a float between -10^9 and 10^9 (inclusive).
"""

import math

def insertion_sort(arr):
    if len(arr) <= 1:
        return arr

    # Divide the array into chunks of size sqrt(n)
    chunk_size = int(math.sqrt(len(arr)))
    chunks = [arr[i:i+chunk_size] for i in range(0, len(arr), chunk_size)]

    # Sort each chunk using insertion sort
    for chunk in chunks:
        for i in range(1, len(chunk)):
            key = chunk[i]
            j = i - 1
            while j >= 0 and chunk[j] > key:
                chunk[j + 1] = chunk[j]
                j -= 1
            chunk[j + 1] = key

    # Merge the sorted chunks
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