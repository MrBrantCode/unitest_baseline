"""
QUESTION:
Create a function `calculate_entropy` that calculates the entropy of a given string representing a quantum state. The function should take a string of 0s and 1s as input, representing the qubits in the quantum state, and return the entropy of the state.
"""

import math
from collections import Counter

def calculate_entropy(qubits):
    # Calculate the probability of each qubit state
    probabilities = [count / len(qubits) for count in Counter(qubits).values()]
    
    # Calculate the entropy
    entropy = -sum([probability * math.log2(probability) for probability in probabilities])
    
    return entropy