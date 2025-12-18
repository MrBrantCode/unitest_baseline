"""
QUESTION:
Implement the `merged_arrays(heap1, heap2)` function to merge two sorted arrays `heap1` and `heap2` into a single sorted array. The function should take two lists of integers as input and return a new list containing all elements from both input lists, sorted in ascending order. The time complexity should be better than O(nlogn), where n is the total number of elements in both heaps.
"""

def merge_sorted_arrays(heap1, heap2):
    """Return combined array with sorted values."""
    merged_heap = []
    i, j = 0, 0

    while i < len(heap1) and j < len(heap2):
        if heap1[i] < heap2[j]:
            merged_heap.append(heap1[i])
            i += 1
        else:
            merged_heap.append(heap2[j])
            j += 1

    while i < len(heap1):
        merged_heap.append(heap1[i])
        i += 1

    while j < len(heap2):
        merged_heap.append(heap2[j])
        j += 1

    return merged_heap