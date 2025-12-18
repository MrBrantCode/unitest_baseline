"""
QUESTION:
Implement a function `rank` that calculates the PageRank for a given graph. The graph should be represented as a dictionary where each key is a node and its corresponding value is a set of its outgoing links. The `rank` function should take the graph, the maximum number of iterations, the damping factor `d`, and the convergence threshold as parameters. It should return a dictionary with the final PageRank for each node. The function should use the PageRank formula and terminate the iteration when the L1 norm of the difference between the new and old ranks is less than the given threshold.
"""

def rank(graph, iters=100, d=0.85, threshold=0.0001):
    """
    Calculate the PageRank for a given graph.

    Args:
    - graph (dict): A dictionary representing the graph where each key is a node and its corresponding value is a set of its outgoing links.
    - iters (int): The maximum number of iterations. Defaults to 100.
    - d (float): The damping factor. Defaults to 0.85.
    - threshold (float): The convergence threshold. Defaults to 0.0001.

    Returns:
    - A dictionary with the final PageRank for each node.
    """

    # Initialize ranks with equal probability
    N = len(graph)
    ranks = {node: 1 / N for node in graph}

    for _ in range(iters):
        # Calculate new ranks using the PageRank formula
        new_ranks = {}
        for page in graph:
            # Calculate the sum of ranks from incoming pages
            rank_sum = sum(ranks[in_page] / len(graph[in_page]) for in_page in graph if page in graph[in_page])
            new_ranks[page] = (1 - d) / N + d * rank_sum

        # Check for convergence using the L1 norm
        l1_norm = sum(abs(new_ranks[page] - ranks[page]) for page in graph)
        if l1_norm < threshold:
            return new_ranks

        # Update ranks for the next iteration
        ranks = new_ranks

    return ranks