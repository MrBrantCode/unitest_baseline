"""
QUESTION:
Implement a function called `generate_superposition_states` that generates all possible superposition states of a qubit given the number of qubits. The function should take an integer `n` representing the number of qubits as input and return a list of all possible superposition states. The function should not take any other input and should not have any side effects.
"""

def generate_superposition_states(n):
    """
    Generates all possible superposition states of a qubit given the number of qubits.

    Args:
        n (int): The number of qubits.

    Returns:
        list: A list of all possible superposition states.
    """

    # Base case: if there is only one qubit, there are two possible states
    if n == 1:
        return ['0', '1']

    # Recursive case: for each state of the first qubit, append all states of the remaining qubits
    else:
        states = generate_superposition_states(n - 1)
        return ['0' + state for state in states] + ['1' + state for state in states]