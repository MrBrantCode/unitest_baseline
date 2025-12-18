"""
QUESTION:
Write a function `find_numbers(array)` that takes an unsorted array of positive integers and returns a tuple containing two lists. The first list should contain the three lowest even numbers in the array, and the second list should contain the three largest odd numbers in the array. If there are less than three even or odd numbers in the array, the function should return an error message indicating the type of numbers that are insufficient. The function should have a good run-time complexity and be able to handle arrays of any size, including empty arrays.
"""

import heapq

def find_numbers(array):
    min_heap = []
    max_heap = []

    for num in array:
        if num % 2 == 0:  # even numbers
            if len(min_heap) < 3:
                heapq.heappush(min_heap, -num)
            else:
                heapq.heappushpop(min_heap, -num)
        else:  # odd numbers
            if len(max_heap) < 3:
                heapq.heappush(max_heap, num)
            else:
                heapq.heappushpop(max_heap, num)

    if len(min_heap) < 3:
        return "Not enough even numbers."
    if len(max_heap) < 3:
        return "Not enough odd numbers."
    return sorted([-i for i in min_heap]), sorted(max_heap, reverse=True)