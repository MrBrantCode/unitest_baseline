"""
QUESTION:
Write a Python function `is_superposition` that determines whether a given qubit can exist in a superposition of states. The function should take as input a dictionary representing the qubit's state, where the keys are the possible states and the values are the corresponding probabilities. The qubit can exist in a superposition of states if the sum of the probabilities is equal to 1 and there is more than one state with a non-zero probability.
"""

def is_superposition(qubit_state):
    """
    Determine whether a given qubit can exist in a superposition of states.

    Args:
    qubit_state (dict): A dictionary representing the qubit's state, 
                        where the keys are the possible states and the values are the corresponding probabilities.

    Returns:
    bool: True if the qubit can exist in a superposition of states, False otherwise.
    """
    # Check if the sum of the probabilities is equal to 1
    sum_probabilities = sum(qubit_state.values())
    
    # Check if there is more than one state with a non-zero probability
    non_zero_states = sum(1 for value in qubit_state.values() if value > 0)
    
    # Return True if both conditions are met, False otherwise
    return abs(sum_probabilities - 1) < 1e-6 and non_zero_states > 1