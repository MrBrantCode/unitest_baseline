"""
QUESTION:
Create a function called `DynamicMinFinder` that can handle a dynamic tuple of integers and find the minimum value in real-time with optimal time complexity. The tuple can contain both positive and negative integer values and its size can change dynamically. The function should be able to add elements, find the minimum value, and delete the minimum value without disrupting the data stream.
"""

import heapq

def DynamicMinFinder(data):
    min_heap = []
    heapq.heapify(min_heap)

    def add_element(element):
        heapq.heappush(min_heap, element)

    def find_min():
        if len(min_heap) == 0:
            return None
        return min_heap[0]

    def delete_min():
        if len(min_heap) == 0:
            return None
        return heapq.heappop(min_heap)

    for num in data:
        add_element(num)

    return find_min, delete_min