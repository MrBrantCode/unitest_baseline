"""
QUESTION:
Write a function called `quantum_superposition` that takes a list of qubits as input, applies quantum superposition to each qubit, and returns a list of qubits in superposition states. The function should be able to handle a list of any length and should not include any error correction techniques.
"""

def quantum_superposition(qubits):
    superposition_states = []
    for qubit in qubits:
        # Assuming qubit is a binary value (0 or 1), apply superposition by making it both 0 and 1
        superposition_states.append([0, 1])
    return superposition_states