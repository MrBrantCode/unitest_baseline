"""
QUESTION:
Generate a function `generate_stabilizer_operators(n)` that takes an integer `n` as input and returns a list of all possible Pauli stabilizer operators for `n` qubits. Each stabilizer operator should be represented as a string of Pauli matrices (e.g., 'IIZX') where each character corresponds to a qubit and represents the Pauli matrix acting on that qubit. Assume that `n` is a positive integer.
"""

from itertools import product

def generate_stabilizer_operators(n):
    pauli_matrices = ['I', 'X', 'Y', 'Z']
    operators = [''.join(p) for p in product(pauli_matrices, repeat=n)]
    return operators