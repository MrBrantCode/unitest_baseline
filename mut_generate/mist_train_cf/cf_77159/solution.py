"""
QUESTION:
Merge k sorted lists into a single sorted list. The function should take a list of lists (where each sublist is a sorted list) as input and return a single sorted list. The solution should be optimized for handling large data sets. Implement a function `mergeKLists(lists)` to solve this problem, where `lists` is a list of sorted lists.
"""

import heapq

def mergeKLists(lists):
    # Initialize the heap with first item from each list
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)
    
    res = []
    while heap:
        val, list_idx, element_idx = heapq.heappop(heap)
        res.append(val)
        
        # If there are remaining elements in the list, push the next onto the heap
        if element_idx + 1 < len(lists[list_idx]):
            next_tuple = (lists[list_idx][element_idx + 1], list_idx, element_idx + 1)
            heapq.heappush(heap, next_tuple)
    return res