"""
QUESTION:
Implement a function named `create_priority_queue` that takes an array of tuples as input and returns the array organized in a priority queue. The priority queue should be ordered based on the first element of each tuple in ascending order. In case of a tie in the first elements, the second elements of the tuples should be in lexicographic increasing order.
"""

import heapq

def create_priority_queue(arr):
    """
    Creates a priority queue from an array of tuples.
    
    The priority queue is ordered based on the first element of each tuple in ascending order.
    In case of a tie in the first elements, the second elements of the tuples are in lexicographic increasing order.

    Args:
        arr (list): A list of tuples.

    Returns:
        list: A list of tuples representing the priority queue.
    """
    # Convert the list into a priority queue
    priority_queue = [(item[0], item[1]) for item in arr]
    heapq.heapify(priority_queue)

    # De-heapify and return the sorted array
    sorted_arr = []
    while priority_queue:
        sorted_arr.append(heapq.heappop(priority_queue))
    return sorted_arr