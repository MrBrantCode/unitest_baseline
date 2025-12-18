"""
QUESTION:
Create a function called `superposition` that takes a list of binary states as input (e.g., [0, 1, 0, 1]) and returns a string representing the superposition of these states in the format of a qubit. The function should not take any other input parameters.
"""

def superposition(states):
    """
    This function takes a list of binary states as input and returns a string 
    representing the superposition of these states in the format of a qubit.

    Args:
        states (list): A list of binary states (0 or 1)

    Returns:
        str: A string representing the superposition of the input states
    """
    return ' '.join(str(state) for state in states)