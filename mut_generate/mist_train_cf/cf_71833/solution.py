"""
QUESTION:
Design a function `isMaxHeap(heap)` to verify if the given array `heap` represents a maximum heap structure or not. The function should be able to handle repeated values in the array, as well as negative numbers and zero. 

If the array does not represent a maximum heap, design a function `buildMaxHeap(heap)` to convert the array into a maximum heap. The function `buildMaxHeap(heap)` should utilize a helper function `heapify(heap, root, n)` to heapify the array. 

Assume that the input array `heap` is a list of integers.
"""

def entance(heap):
    n = len(heap)
    for i in range(int(n/2)-1, -1, -1):
        j = 2 * i + 1
        while j < n:
            if j + 1 < n and heap[j+1] > heap[j]:
                j += 1
            if heap[i] < heap[j]:
                return False
            j *= 2
    return True

def buildMaxHeap(heap):
    n = len(heap)
    for i in range(int(n/2)-1, -1, -1):
        heapify(heap, i, n)
    return heap

def heapify(heap, root, n):
    largest = root
    left = 2 * root + 1
    right = 2 * root + 2
    if left < n and heap[left] > heap[largest]:
        largest = left
    if right < n and heap[right] > heap[largest]:
        largest = right
    if largest != root:
        heap[root], heap[largest] = heap[largest], heap[root]
        heapify(heap, largest, n)