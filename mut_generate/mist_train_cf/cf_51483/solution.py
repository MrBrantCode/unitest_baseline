"""
QUESTION:
Implement a function `quick_sort` that takes a double-ended queue (`deque`) and sorts its elements using the QuickSort algorithm. The `quick_sort` function should modify the original deque in-place. The input deque can be of any size, and the elements can be in any order.
"""

from collections import deque

def partition(deq, l, h):
    i = l - 1
    pivot = deq[h]

    for j in range(l, h):
        if deq[j] <= pivot:
            i += 1
            deq[i], deq[j] = deq[j], deq[i]

    deq[i+1], deq[h] = deq[h], deq[i+1]
    return i+1


def quick_sort(deq, low, high):
    if len(deq) == 1:
        return deq
    if low < high:
        pi = partition(deq, low, high)

        quick_sort(deq, low, pi-1)
        quick_sort(deq, pi+1, high)