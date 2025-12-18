"""
QUESTION:
Write a function `median` that calculates the median of a list of numbers without sorting the list. The function should work with lists containing negative integers, floating-point numbers, and both odd and even counts of numbers. The function should return the median as a floating-point number if the list has an even count of numbers.
"""

import heapq

def median(lst: list):
    max_heap = []
    min_heap = []
    length = len(lst)
    for num in lst:
        if len(max_heap) == 0 or num < -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)
        if len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))
        if len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
    if length % 2 == 1:
        return -max_heap[0]
    else:
        return (-max_heap[0] + min_heap[0]) / 2