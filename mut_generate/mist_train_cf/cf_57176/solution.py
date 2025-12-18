"""
QUESTION:
Create a function `quantum_entanglement` that calculates the correlation between two qubits in an entangled state. The function should take two integers `qubit1` and `qubit2` as input, each representing the state of a qubit (0 or 1), and return their correlation. Assume the qubits are maximally entangled in a Bell state.
"""

def quantum_entanglement(qubit1, qubit2):
    if qubit1 == qubit2:
        return -1
    else:
        return 1