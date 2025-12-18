"""
QUESTION:
Implement the `build_min_heap(a)` function to convert a given array of integers into a min-heap. The function should take an array `a` of integers as input, where `1 <= len(a) <= 10^5`, and return the resulting min-heap array. A min-heap is a complete binary tree where the value of each node is less than or equal to the values of its children.
"""

def build_min_heap(a):
    def heapify(arr, n, i):
        smallest = i
        left = 2 * i + 1
        right = 2 * i + 2

        if left < n and arr[i] > arr[left]:
            smallest = left

        if right < n and arr[smallest] > arr[right]:
            smallest = right

        if smallest != i:
            arr[i], arr[smallest] = arr[smallest], arr[i]
            heapify(arr, n, smallest)

    n = len(a)
    for i in range(n // 2 - 1, -1, -1):
        heapify(a, n, i)
    return a