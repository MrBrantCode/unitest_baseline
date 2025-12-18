"""
QUESTION:
Write a function `remove_epsilon(input_string: str) -> str` that takes a string representing a finite-state acceptor in OpenFst format, where each line represents a transition in the format "source_state destination_state label weight", and returns the modified acceptor string with all epsilon transitions (label '0') removed.
"""

def remove_epsilon(input_string: str) -> str:
    lines = input_string.strip().split('\n')
    transitions = [line.split() for line in lines]
    non_epsilon_transitions = [t for t in transitions if t[2] != '0']
    return '\n'.join([' '.join(t) for t in non_epsilon_transitions])