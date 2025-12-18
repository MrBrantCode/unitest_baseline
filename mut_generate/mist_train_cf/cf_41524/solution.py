"""
QUESTION:
Implement a function `insert_node` that takes in a sorted list of assignments and a new node. Each assignment is a tuple containing a string representing the assignment name and an integer representing the priority of the assignment. The function should insert the new node into the list of assignments at the correct position based on the node's priority value, maintaining the sorted order in ascending order. The function should return the updated list of assignments.
"""

from typing import List, Tuple

def insert_node(assignments: List[Tuple[str, int]], new_node: Tuple[str, int]) -> List[Tuple[str, int]]:
    index = 0
    for i, (_, priority) in enumerate(assignments):
        if new_node[1] < priority:
            index = i
            break
    else:
        index = len(assignments)
    assignments.insert(index, new_node)
    return assignments