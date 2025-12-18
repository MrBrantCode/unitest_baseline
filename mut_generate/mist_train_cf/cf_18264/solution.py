"""
QUESTION:
Design a function `k_closest_elements` that takes a sorted array `arr`, a target value `target`, and a positive integer `k` as input, and returns the k closest elements to the target value in ascending order based on their absolute difference. The function should be efficient and have a time complexity of O(n log k) and a space complexity of O(k).
"""

import heapq

def k_closest_elements(arr, target, k):
    """
    Returns the k closest elements to the target value in a sorted array.

    Args:
        arr (list): A sorted list of integers.
        target (int): The target value.
        k (int): The number of closest elements to find.

    Returns:
        list: A list of the k closest elements to the target value in ascending order.
    """
    # Initialize an empty min heap to store the k closest elements
    min_heap = []

    # Iterate through each element in the sorted array
    for num in arr:
        # Calculate the absolute difference between the element and the target value
        diff = abs(num - target)

        # If the min heap has less than k elements, add the current element to the min heap
        if len(min_heap) < k:
            heapq.heappush(min_heap, (-diff, num))
        # If the min heap has k elements, compare the absolute difference of the current element with the top element of the min heap
        elif diff < -min_heap[0][0]:
            heapq.heappop(min_heap)
            heapq.heappush(min_heap, (-diff, num))

    # Pop all the elements from the min heap and store them in a list in ascending order
    closest_elements = sorted([num for diff, num in min_heap])

    return closest_elements