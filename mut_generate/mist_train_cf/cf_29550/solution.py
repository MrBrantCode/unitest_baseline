"""
QUESTION:
Implement a `MaxHeap` class with methods `add(x)` and `find_max()`. The `add(x)` method should add the integer `x` to the data structure. The `find_max()` method should return the maximum element in the data structure without removing it. You must use the `heapq` module and a max-heap data structure. Ensure that the `find_max()` method returns `None` if the data structure is empty.
"""

import heapq

def entrance(nums):
    maxheap = []
    for num in nums:
        heapq.heappush(maxheap, -num)
    if maxheap:
        return -maxheap[0]
    else:
        return None