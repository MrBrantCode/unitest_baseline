"""
QUESTION:
Implement the function `hybrid_sort_list_heap(lst)` that takes a list of integers and decimals, uses a heap sort combined with another sorting algorithm to arrange the list in a special order. The ordering should start with the smallest value, then the largest, then the smallest of the remaining values not yet included in the output, and continue doing this until all elements are sorted. Ensure the second sorting algorithm is utilized in a way that enhances the efficiency of the solution. The second sorting algorithm should be used for smaller size subarrays and heap sort for larger size ones.
"""

import heapq
import bisect

def hybrid_sort_list_heap(lst):
    heapq.heapify(lst)

    if len(lst) < 10:
        sorted_lst = binary_insertion_sort(lst)
    else:
        sorted_lst = [heapq.heappop(lst) for _ in range(len(lst))]

    result = []
    while sorted_lst:
        result.append(sorted_lst.pop(0))  
        if sorted_lst:
            result.append(sorted_lst.pop(-1))  

    return result

def binary_insertion_sort(arr):
    for i in range(1, len(arr)):
        bisect.insort(arr, arr.pop(i), 0, i)
    return arr