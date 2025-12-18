"""
QUESTION:
Implement a function named `modified_heapsort(arr)` that sorts an array of integers using a modified version of the heapsort algorithm with a min-heap data structure. The function should take an array of integers as input and return the sorted array. The time complexity of the algorithm should be O(n log k), where n is the length of the input array and k is the number of distinct elements in the input array.
"""

import heapq

def modified_heapsort(arr):
    # Step 1: Build a min-heap using the input array
    heapq.heapify(arr)

    # Step 2: Create an empty result array
    result = []

    # Step 3: Extract minimum elements from the min-heap
    while arr:
        min_val = heapq.heappop(arr)
        result.append(min_val)

        # Check for duplicates and extract them as well
        while arr and arr[0] == min_val:
            result.append(heapq.heappop(arr))

    # Step 4: Return the result array
    return result