"""
QUESTION:
Write a function `complex_median` that calculates the median of a list of numbers without sorting the list, handling cases with an even or odd number of elements. The function should use a max heap and a min heap to efficiently compute the median in constant time. The heaps should be balanced, meaning their lengths should not differ by more than one. If the length of the max heap is greater than the length of the min heap, return the top element of the max heap as a float. If the lengths are equal, return the average of the top elements of both heaps.
"""

import heapq

def complex_median(lst):
    max_heap = [] 
    min_heap = [] 

    def add_number(num):
        if len(max_heap) == 0 or num < -max_heap[0]:
            heapq.heappush(max_heap, -num)
        else:
            heapq.heappush(min_heap, num)

    def rebalance():
        if len(max_heap) < len(min_heap):
            number = heapq.heappop(min_heap)
            heapq.heappush(max_heap, -number)
        elif len(max_heap) > len(min_heap) + 1:
            number = -heapq.heappop(max_heap)
            heapq.heappush(min_heap, number)

    def get_median():
        if len(max_heap) > len(min_heap):
            return float(-max_heap[0])
        else:
            return (min_heap[0] - max_heap[0]) / 2.0

    for num in lst:
        add_number(num)
        rebalance()

    return get_median()