"""
QUESTION:
Implement a function `find_kth_largest(nums, k)` that takes an array `nums` and an integer `k` as input and returns the kth largest element in the array. The function must use a min heap data structure without utilizing built-in sorting or priority queue functions and without using extra space to store the heap. The time complexity of the algorithm should be O(n log k) and the space complexity should be O(1).
"""

def find_kth_largest(nums, k):
    heap = []

    for num in nums:
        if len(heap) < k:
            heap.append(num)
            if len(heap) == k:
                # Convert list to min heap
                for i in range(k//2 - 1, -1, -1):
                    heapify(heap, k, i)
        elif num > heap[0]:
            heap[0] = num
            heapify(heap, k, 0)
    
    return heap[0]

def heapify(heap, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and heap[left] < heap[smallest]:
        smallest = left
    if right < n and heap[right] < heap[smallest]:
        smallest = right
    
    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        heapify(heap, n, smallest)