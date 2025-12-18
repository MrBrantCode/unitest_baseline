"""
QUESTION:
Write a function `k_most_common` that takes an array of integers and an integer `k` as input, and returns the k most common elements in the array. The function should have a time complexity of O(nlogk), where n is the size of the array.
"""

import heapq

def k_most_common(nums, k):
    """
    Returns the k most common elements in the array.

    Args:
        nums (list): A list of integers.
        k (int): The number of most common elements to return.

    Returns:
        list: A list of the k most common elements in descending order of frequency.
    """

    # Create a dictionary to store the frequency count of each element
    freq_dict = {}
    for num in nums:
        if num not in freq_dict:
            freq_dict[num] = 1
        else:
            freq_dict[num] += 1

    # Create a min heap to store the k most common elements
    min_heap = []
    for num, freq in freq_dict.items():
        if len(min_heap) < k:
            heapq.heappush(min_heap, (freq, num))
        else:
            if freq > min_heap[0][0]:
                heapq.heappop(min_heap)
                heapq.heappush(min_heap, (freq, num))

    # Create a list to store the k most common elements in descending order
    result = []
    while min_heap:
        freq, num = heapq.heappop(min_heap)
        result.insert(0, num)

    return result