"""
QUESTION:
Implement a function named `quick_sort` that takes a double-ended queue (deque) as input and returns a sorted deque using the QuickSort algorithm. The function should handle deques of any length, including empty or single-element deques, which are considered sorted. The function should not modify the original deque and instead return a new sorted deque.
"""

from collections import deque

def quick_sort(de):
    if len(de) <= 1:
        return de
    else:
        pivot = de[0]
        lesser = deque(x for x in de if x < pivot)
        equal = deque(x for x in de if x == pivot)
        greater = deque(x for x in de if x > pivot)
        return quick_sort(lesser) + equal + quick_sort(greater)