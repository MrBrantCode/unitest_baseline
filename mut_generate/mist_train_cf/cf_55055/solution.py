"""
QUESTION:
Implement a function called `is_superposition` that takes in a list of qubits, each represented as a dictionary with keys 'state' and 'value', and returns a boolean indicating whether the qubits are in a state of superposition.
"""

def is_superposition(qubits):
    for qubit in qubits:
        if qubit['state'] == 'superposition' or (qubit['value'] != 0 and qubit['value'] != 1):
            return True
    return False