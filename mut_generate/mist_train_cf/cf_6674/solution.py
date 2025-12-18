"""
QUESTION:
Create a function `find_top_k_numbers(nums, k)` that takes a list of numbers (`nums`) and a positive integer (`k`) as parameters and returns the top k biggest distinct numbers in descending order. The function should have a time complexity of O(n log k), where n is the length of the given list.
"""

import heapq

def entrance(nums, k):
    """
    Returns the top k biggest distinct numbers in descending order.

    Args:
    - nums (list): A list of numbers.
    - k (int): A positive integer.

    Returns:
    - list: The top k biggest distinct numbers in descending order.
    """
    distinct_nums = list(set(nums))  # Remove duplicates
    heap = []
    
    # Create a min heap
    for num in distinct_nums:
        heapq.heappush(heap, num)
    
    # Pop the smallest numbers from the heap until we have k largest numbers left
    for _ in range(len(distinct_nums) - k):
        heapq.heappop(heap)
    
    # The heap now contains the top k numbers, but in ascending order
    # We need to reverse it to get the numbers in descending order
    top_k_numbers = []
    while heap:
        top_k_numbers.append(heapq.heappop(heap))
    
    # Reverse the list to get the numbers in descending order
    return top_k_numbers[::-1]