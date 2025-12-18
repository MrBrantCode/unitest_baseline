"""
QUESTION:
Determine the number of independent variables in a three-state Hidden Markov Model (HMM) with the specified architecture X --> Y --> Z. Note that the concept of independent variables in HMMs is different from traditional statistical methods; for this purpose, consider each state as a categorical independent variable.
"""

def num_independent_variables(num_states):
    """
    Determine the number of independent variables in a Hidden Markov Model (HMM).

    Args:
    num_states (int): The number of states in the HMM.

    Returns:
    int: The number of independent variables in the HMM.
    """
    return num_states