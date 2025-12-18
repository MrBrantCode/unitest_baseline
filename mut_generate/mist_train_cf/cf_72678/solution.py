"""
QUESTION:
Write a function called `is_superposition` that takes a list of states as input and returns a boolean indicating whether the states represent a superposition. The function should accept a list of integers, and the states should be represented as integers. A superposition is represented by more than one state, and all states must be different.
"""

def is_superposition(states):
    """
    Checks if a list of states represents a superposition.

    A superposition is represented by more than one state, and all states must be different.

    Args:
    states (list): A list of integers representing the states.

    Returns:
    bool: True if the states represent a superposition, False otherwise.
    """
    return len(states) > 1 and len(states) == len(set(states))