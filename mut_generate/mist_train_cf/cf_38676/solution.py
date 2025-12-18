"""
QUESTION:
Implement a function `compute_dominance_frontier(head)` that takes the head node of a control flow graph and returns a dictionary where the keys are nodes and the values are the sets of nodes representing the dominance frontier for each node. The function should use the following attributes and methods of the control flow graph: `nodes`, `edges`, `dominators`, `predecessors`, and `successors`.
"""

def compute_dominance_frontier(head):
    """
    Compute the dominance frontier for each node in the control flow graph.

    Args:
    head (ControlFlowGraph): The head node of the control flow graph.

    Returns:
    dict: A dictionary where the keys are nodes and the values are the sets of nodes representing the dominance frontier for each node.
    """
    dominance_frontier = {node: set() for node in head.nodes}

    for node in head.nodes:
        if len(head.successors[node]) > 1:
            for successor in head.successors[node]:
                runner = successor
                while runner != head.dominators[node]:
                    dominance_frontier[runner].add(node)
                    runner = head.dominators[runner]

    return dominance_frontier