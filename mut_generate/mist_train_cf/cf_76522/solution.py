"""
QUESTION:
Implement a function named `strange_sort_list_heap` that takes a list of integers and decimals as input. The function should use a heap sort to arrange the list in a peculiar order, starting with the smallest value, then the largest value, then the smallest of the remaining values not yet included in the output, and repeat this process until all elements are sorted. The input list can be empty.
"""

import heapq

def strange_sort_list_heap(lst):
    # Base case for an empty list
    if not lst:
        return []
    
    # Transform list into a heap, in-place, in O(len(lst)) time
    heapq.heapify(lst)
    
    # List to hold the final result
    result = []
    
    # Flag to check whether to pop smallest or largest number
    pop_smallest = True
    
    while lst:
        if pop_smallest:  # Pop the smallest number
            result.append(heapq.heappop(lst))  # heapq.heappop() pops and return smallest element from heap
        else:  # Pop the largest number
            lst = [-i for i in lst]  # Invert the order of heap
            heapq.heapify(lst)  # Heapify again as order has changed
            result.append(-heapq.heappop(lst))  # heapq.heappop() pops and return smallest(negative of largest) element from heap
            lst = [-i for i in lst]  # Invert the order back
            heapq.heapify(lst)  # Heapify again as order has changed
        # Invert the flag to pop the other number in next iteration
        pop_smallest = not pop_smallest
        
    return result