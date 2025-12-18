"""
QUESTION:
Implement a function `processTasks` that takes a list of tasks with their respective priorities as input and processes them in order of their priorities. The function should use a priority queue data structure to achieve an efficient time complexity of O(log n) or better. The input list of tasks is a list of tuples, where each tuple contains the priority and the task. The function should return the tasks in the order they were processed.
"""

import heapq

def processTasks(tasks):
    """
    Process tasks in order of their priorities using a priority queue.

    Args:
        tasks (list): A list of tuples, where each tuple contains the priority and the task.

    Returns:
        list: The tasks in the order they were processed.
    """
    priority_queue = []
    processed_tasks = []

    # Push elements with their respective priorities into the priority queue
    for priority, task in tasks:
        heapq.heappush(priority_queue, (priority, task))

    # Pop and process the highest priority element
    while priority_queue:
        priority, task = heapq.heappop(priority_queue)
        processed_tasks.append(task)

    return processed_tasks