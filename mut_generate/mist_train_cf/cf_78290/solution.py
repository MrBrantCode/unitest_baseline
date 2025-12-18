"""
QUESTION:
Write a function named `heap_sort_descending` that takes a list of numbers as input and returns a new list containing the numbers in descending order, using a heap-based algorithm. The input list is a collection of numbers from multiple sets, which are combined into one list. Implement the function using Python's heapq module and simulate a max heap by pushing the negatives of the numbers into the heap. Analyze the time and space complexity of the function.
"""

import heapq

def heap_sort_descending(nums):
    heap = []
    for num in nums:
        heapq.heappush(heap, -num)
    sorted_nums = []
    while heap:
        sorted_nums.append(-heapq.heappop(heap))
    return sorted_nums