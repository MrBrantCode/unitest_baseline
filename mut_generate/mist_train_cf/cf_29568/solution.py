"""
QUESTION:
Implement a function `find_problematic_positions` that takes in a list of directed edges in a graph and a list of last positions visited in a traversal algorithm. The function returns a list of positions where there is not exactly one edge from the last position. 

The input `edges` is a list of tuples, where each tuple `(u, v)` represents a directed edge from node `u` to node `v`. The input `last_pos` is a list of integers, where `last_pos[i]` is the last position visited at step `i`. 

The function should return a list of integers representing the positions where the algorithm encounters the problem of having either zero or more than one edge pointing back to the last position.
"""

from typing import List, Tuple

def find_problematic_positions(edges: List[Tuple[int, int]], last_pos: List[int]) -> List[int]:
    problematic_positions = []
    for i in range(len(last_pos)):
        count = sum(1 for edge in edges if edge[0] == last_pos[i])
        if count != 1:
            problematic_positions.append(i+1)
    return problematic_positions