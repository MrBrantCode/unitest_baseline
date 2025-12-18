"""
QUESTION:
Derive the maximum likelihood estimator of transition probabilities in a discrete time and space Markov chain. The transition probabilities should be represented as $p_{ij}$, where $i$ and $j$ are states, and $n_{ij}$ is the number of transitions from $i$ to $j$. The estimator should be derived from the likelihood function $L(p) = \prod_{i\in S}\prod_{j \in S} {p_{ij}}^{n_{ij}}$ and be subject to the constraints that $p_{ij}$ is a probability, i.e., $p_{ij}\geq0$ and $\sum_{j \in S} p_{ij} = 1$.
"""

def estimate_transition_probabilities(transitions):
    """
    Estimate transition probabilities in a discrete time and space Markov chain.

    Parameters:
    transitions (dict): A dictionary where the keys are the source states and the values are dictionaries
                        where the keys are the destination states and the values are the number of transitions.

    Returns:
    dict: A dictionary where the keys are the source states and the values are dictionaries
          where the keys are the destination states and the values are the estimated transition probabilities.
    """
    transition_probabilities = {}
    for source_state, destinations in transitions.items():
        total_transitions = sum(destinations.values())
        transition_probabilities[source_state] = {destination: transitions / total_transitions for destination, transitions in destinations.items()}
    return transition_probabilities