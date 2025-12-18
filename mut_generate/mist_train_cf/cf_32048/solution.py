"""
QUESTION:
Implement the `find_slice_at_step` function to return the sliced graph at a given step in the process, where the sliced graph is determined by the provided ordering of nodes and the graph structure, and the step is represented by the `p_bunch` parameter.

The function should take three parameters: 
- `ordering`: a list representing the ordering of nodes in the graph
- `graph`: a dictionary representing the graph structure
- `p_bunch`: an integer representing the step in the process

The function should return the sliced graph at the given step as a dictionary.
"""

def find_slice_at_step(ordering, graph, p_bunch):
    """
    Parameters:
    ordering: list - A list representing the ordering of nodes in the graph
    graph: dict - A dictionary representing the graph structure
    p_bunch: int - An integer representing the step in the process

    Returns:
    graph: dict - The sliced graph at the given step
    """
    sliced_graph = {}
    for i, node in enumerate(ordering):
        if i < p_bunch:
            sliced_graph[node] = graph[node]
    return sliced_graph