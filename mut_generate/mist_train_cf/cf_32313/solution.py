"""
QUESTION:
Write a function `update_counts` that takes a list of edges and their corresponding colors, and returns the final counts of monochromatic and bichromatic edges after processing all the edges. 

Function Signature: `def update_counts(edges: List[Tuple[int, int]], colors: List[str]) -> Tuple[int, int]`

Input:
- `edges`: a list of tuples, where each tuple represents an edge in an undirected graph. Each tuple contains two integers `u` and `v` (1 <= u, v <= n), representing the vertices of the edge.
- `colors`: a list of strings, where `colors[i]` represents the color of vertex `i+1` (either 'R' for red or 'B' for blue).

Output:
- A tuple containing two integers: the count of monochromatic edges and the count of bichromatic edges, in that order.

Restrictions: 
- The graph is undirected, and the edges are not repeated in the input list.
- The colors of the vertices are either 'R' or 'B'.
"""

from typing import List, Tuple

def update_counts(edges: List[Tuple[int, int]], colors: List[str]) -> Tuple[int, int]:
    monochromatic = 0
    bichromatic = 0
    for edge in edges:
        if colors[edge[0]-1] == colors[edge[1]-1]:
            monochromatic += 1
        else:
            bichromatic += 1
    return monochromatic, bichromatic