"""
QUESTION:
Implement a function `median(my_list, new_element)` that finds the median of an unsorted array after inserting a new element into the array. The array will not contain duplicates and will have at least one element. The function should handle arrays of up to 10^6 elements efficiently. The median calculation should consider whether the array's length is even or odd, and the function should maintain a sorted array. The function should return the updated median of the array after the new element is added in the correct position.
"""

import heapq

def median(my_list, new_element):
    max_heap = []  # stores first half
    min_heap = []  # stores second half
    
    # Create initial heaps from input list
    for num in my_list:
        # if new element is larger than highest in 1st half, push it into 2nd half
        if len(max_heap) > 0 and num > -max_heap[0]:
            heapq.heappush(min_heap, num)
        else:
            heapq.heappush(max_heap, -num)

        # if heap sizes are unequal, balance them by transferring element
        if len(min_heap) > len(max_heap):
            heapq.heappush(max_heap, -heapq.heappop(min_heap))
        elif len(max_heap) > len(min_heap) + 1:
            heapq.heappush(min_heap, -heapq.heappop(max_heap))

    # Add the new element into the heaps
    if len(max_heap) > 0 and new_element > -max_heap[0]:
        heapq.heappush(min_heap, new_element)
    else:
        heapq.heappush(max_heap, -new_element)

    # Balance the heaps
    if len(min_heap) > len(max_heap):
        heapq.heappush(max_heap, -heapq.heappop(min_heap))
    elif len(max_heap) > len(min_heap) + 1:
        heapq.heappush(min_heap, -heapq.heappop(max_heap))

    # Median calculation
    if len(min_heap) == len(max_heap):
        return (-max_heap[0] + min_heap[0]) / 2.0
    else:
        return -max_heap[0]