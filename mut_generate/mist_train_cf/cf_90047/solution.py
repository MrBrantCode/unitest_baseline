"""
QUESTION:
Implement a function `heapsort` that sorts a list of at least 100 integers (positive and negative) in descending order using heapsort. The function should handle cases with duplicate elements, already sorted lists, and lists containing floating-point numbers, with a time complexity of O(n log n).
"""

import heapq

def heapsort(lst):
    # Convert floating-point numbers to negative infinity
    lst = [-float('inf') if isinstance(x, float) else x for x in lst]
    heapq.heapify(lst)
    sorted_lst = []
    while lst:
        sorted_lst.append(heapq.heappop(lst))
    # Convert negative infinity back to floating-point numbers
    sorted_lst = [float('-inf') if x == -float('inf') else x for x in sorted_lst]
    return sorted_lst[::-1]