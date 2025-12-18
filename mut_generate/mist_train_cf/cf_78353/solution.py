"""
QUESTION:
Compute the conditional probability $p(F|A)$ in a directed cyclic graph where vertex A is 'infected' and each edge has a different infection probability. The function should be named `compute_conditional_probability`. The graph can be very large, so the algorithm should be computationally feasible.
"""

def compute_conditional_probability(graph, probabilities, node):
    """
    Compute the conditional probability of infection in a directed cyclic graph.

    Parameters:
    graph (dict): Adjacency list representation of the graph.
    probabilities (dict): Infection probabilities for each edge.
    node (str): The 'infected' node.

    Returns:
    float: The conditional probability of infection.
    """
    # Implementation details will vary based on the chosen approach.
    # For demonstration purposes, a simple example using a Markov process is shown.

    # Initialize the infection probability for the given node to 1
    infection_probabilities = {node: 1}

    # Simulate the Markov process
    for _ in range(100):  # Number of simulation trials
        new_probabilities = {}
        for current_node, neighbors in graph.items():
            if current_node in infection_probabilities:
                for neighbor in neighbors:
                    if neighbor not in new_probabilities:
                        new_probabilities[neighbor] = 0
                    new_probabilities[neighbor] += infection_probabilities[current_node] * probabilities[(current_node, neighbor)]
        infection_probabilities = new_probabilities

    # Compute the conditional probability
    conditional_probability = sum(infection_probabilities.values())

    return conditional_probability