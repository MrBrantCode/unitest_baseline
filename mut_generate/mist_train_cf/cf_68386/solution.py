"""
QUESTION:
Given a Bayesian network with variables H, U, P, and W, where the relationships between the variables are defined as H --> U <-- P <-- W, calculate the total number of independent parameters required for the network assuming all variables can take an arbitrary number of states.
"""

def calculate_independent_parameters(variables, parents, states):
    """
    Calculate the total number of independent parameters required for a Bayesian network.

    Args:
    - variables (list): A list of variable names.
    - parents (dict): A dictionary where keys are variable names and values are lists of parent variable names.
    - states (dict): A dictionary where keys are variable names and values are the number of states each variable can take.

    Returns:
    - int: The total number of independent parameters required for the network.
    """
    total_parameters = 0
    for variable in variables:
        parent_states = 1
        for parent in parents[variable]:
            parent_states *= states[parent]
        total_parameters += (states[variable] * parent_states) - 1
    return total_parameters

def entrance(variables, parents, states):
    return calculate_independent_parameters(variables, parents, states)