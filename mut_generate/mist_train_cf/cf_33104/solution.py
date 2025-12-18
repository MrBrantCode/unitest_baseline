"""
QUESTION:
Write a function `update_tabu_edges` that takes the following parameters:
- `idx_group`: A list of integers representing the vertex indices to be added to or removed from the tabu edges.
- `tabu_edges`: A list of tuples, each representing a tabu edge as a pair of vertex indices.
- `tabu_idx_group`: A boolean flag indicating whether the `idx_group` should be added to (True) or removed from (False) the tabu edges.

The function should return the updated list of tabu edges after applying the changes based on the input parameters. The function should assume that `idx_group` contains at least two elements and that the pairs of vertex indices from `idx_group` are ordered, i.e., for any pair (i, i+1), i is the first element and i+1 is the second element.
"""

from typing import List, Tuple

def update_tabu_edges(
    idx_group: List[int],
    tabu_edges: List[Tuple[int, int]],
    tabu_idx_group: bool,
) -> List[Tuple[int, int]]:
    if tabu_idx_group:
        updated_tabu_edges = tabu_edges + [(idx_group[i], idx_group[i+1]) for i in range(len(idx_group)-1)]
    else:
        updated_tabu_edges = [edge for edge in tabu_edges if edge not in [(idx_group[i], idx_group[i+1]) for i in range(len(idx_group)-1)]]
    return updated_tabu_edges