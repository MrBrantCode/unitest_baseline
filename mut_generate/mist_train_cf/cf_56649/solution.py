"""
QUESTION:
Write a function `kth_smallest_even(nums, k)` that takes a list of integers `nums` and an integer `k` as input, and returns the k-th smallest even number in the list. The function should be efficient enough to handle large sets of data (up to 10^5 integers) and should have optimal time and space complexity. The input list `nums` has a length of 1 to 10^5, and `k` is an integer between 1 and 100. If there are less than `k` even numbers in the list, the function should return `None`.
"""

import heapq

def kth_smallest_even(nums, k):
    even_nums = [num for num in nums if num % 2 == 0]
    if k > len(even_nums):
        return None
    heapq.heapify(even_nums)
    result = None
    for _ in range(k):
        result = heapq.heappop(even_nums)
    return result