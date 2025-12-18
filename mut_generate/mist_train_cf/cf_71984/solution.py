"""
QUESTION:
Write a function `strange_sort_list_heap(lst)` that takes a list of integers as input and returns a new list containing the same integers sorted in a "strange" order: the smallest number, the largest number, the second smallest number, the second largest number, and so on. The function must use a heap data structure.
"""

import heapq

def strange_sort_list_heap(lst):
    if not lst:
        return []

    heapq.heapify(lst)

    result = []
    pop_smallest = True

    while lst:
        if pop_smallest:  
            result.append(heapq.heappop(lst))  
        else:  
            lst = [-i for i in lst]  
            heapq.heapify(lst)  
            result.append(-heapq.heappop(lst))  
            lst = [-i for i in lst]  
            heapq.heapify(lst)  

        pop_smallest = not pop_smallest

    return result