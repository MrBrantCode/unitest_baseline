"""
QUESTION:
Calculate the median of a list without sorting the list. The list can contain both an even and odd number of elements. The function should return the median as a float if the list has an even number of elements, and as an integer if the list has an odd number of elements.
"""

import heapq

def calculate_median(l: list):
    minHeap, maxHeap = [], []
    
    for num in l:
        if len(minHeap) == len(maxHeap):
            if maxHeap and num < -maxHeap[0]:
                heapq.heappush(minHeap, -heapq.heappop(maxHeap))
                heapq.heappush(maxHeap, -num)
            else:
                heapq.heappush(minHeap, num)
        else:
            if num > minHeap[0]:
                heapq.heappush(maxHeap, -heapq.heappop(minHeap))
                heapq.heappush(minHeap, num)
            else:
                heapq.heappush(maxHeap, -num)

    if len(minHeap) == len(maxHeap):
        median = (minHeap[0] - maxHeap[0]) / 2.0
    else:
        median = minHeap[0]

    return median