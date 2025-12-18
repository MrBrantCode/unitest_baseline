"""
QUESTION:
Write a function called `superposition_simulation` that simulates the concept of quantum superposition, where a quantum system can be in all possible states at once until measured. The function should take in a list of possible states and return a dictionary where the keys are the possible states and the values are the probabilities of each state. The probabilities should be equally distributed among all states.
"""

def superposition_simulation(states):
    """
    Simulates the concept of quantum superposition by distributing probabilities equally among all possible states.

    Args:
        states (list): A list of possible states in the quantum system.

    Returns:
        dict: A dictionary where the keys are the possible states and the values are the probabilities of each state.
    """
    # Calculate the probability of each state by dividing 1 by the total number of states
    probability = 1 / len(states)
    
    # Use dictionary comprehension to create a dictionary where each state is a key and its corresponding value is the probability
    return {state: probability for state in states}