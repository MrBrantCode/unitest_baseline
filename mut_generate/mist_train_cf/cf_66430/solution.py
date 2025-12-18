"""
QUESTION:
Implement a function named `merge_sorted_lists` that takes in a list of k sorted lists as input and returns a single sorted list containing all elements from the input lists. The function should be optimized for time complexity, specifically achieving O(n log k) where n is the total number of elements in all the lists and k is the number of lists.
"""

import heapq

def merge_sorted_lists(lists):
    heap = [(lst[0], i, 0) for i, lst in enumerate(lists) if lst]
    heapq.heapify(heap)
    merged_list = []
    
    while heap:
        val, list_ind, element_ind = heapq.heappop(heap)

        merged_list.append(val)

        if element_ind + 1 < len(lists[list_ind]):
            next_tuple = (lists[list_ind][element_ind + 1],
                          list_ind,
                          element_ind + 1)
            heapq.heappush(heap, next_tuple)
    return merged_list