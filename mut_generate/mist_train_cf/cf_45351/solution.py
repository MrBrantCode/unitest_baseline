"""
QUESTION:
Find the kth smallest element in an unsorted array using a method with a time complexity of O(n log k). The function, `findKthSmallest`, takes two parameters: an unsorted array of integers and an integer k representing the kth smallest element to be found. The array contains at least k distinct elements and k is 1-indexed.
"""

import heapq

def findKthSmallest(nums, k):
    """
    Find the kth smallest element in an unsorted array using a max heap.

    Args:
    nums (list): The unsorted array of integers.
    k (int): The kth smallest element to be found (1-indexed).

    Returns:
    int: The kth smallest element in the array.
    """

    # Create an empty max heap (priority queue)
    max_heap = []

    # Iterate over the first k elements of the array and add them into the max heap
    for num in nums[:k]:
        heapq.heappush(max_heap, -num)  # Use negative numbers to simulate a max heap

    # Iterate the array from the (k+1)th element to the end of the array
    for num in nums[k:]:
        # If the current number is less than the top element of the max heap,
        # remove the top element and add the current number into the heap
        if num < -max_heap[0]:
            heapq.heappop(max_heap)
            heapq.heappush(max_heap, -num)

    # The top of the max heap will be the kth smallest element
    return -max_heap[0]