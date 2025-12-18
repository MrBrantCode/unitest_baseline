"""
QUESTION:
Implement the `external_merge_sort` function that sorts a list of integers in ascending order, without using any built-in sorting functions or data structures. The function should have a time complexity of O(n log n), be stable, and handle duplicate values correctly. The algorithm should also be able to sort large data sets that cannot fit entirely in memory, by dividing the data into smaller chunks that can fit in memory, sorting them individually, and merging the sorted chunks to produce the final sorted result. The function should take a list of integers as input and return the sorted list.
"""

import heapq

def external_merge_sort(data):
    chunk_size = 10000  # adjust this value based on available memory
    chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]
    
    sorted_chunks = []
    for chunk in chunks:
        sorted_chunks.append(sorted(chunk))
    
    return merge_sorted_chunks(sorted_chunks)


def merge_sorted_chunks(sorted_chunks):
    min_heap = []
    for i, chunk in enumerate(sorted_chunks):
        if chunk:
            heapq.heappush(min_heap, (chunk[0], i, 0))
    
    result = []
    while min_heap:
        val, chunk_index, element_index = heapq.heappop(min_heap)
        result.append(val)
        
        if element_index + 1 < len(sorted_chunks[chunk_index]):
            next_tuple = (sorted_chunks[chunk_index][element_index + 1], chunk_index, element_index + 1)
            heapq.heappush(min_heap, next_tuple)
    
    return result