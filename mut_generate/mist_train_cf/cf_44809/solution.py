"""
QUESTION:
Implement a function `quantum_teleportation` to simulate the teleportation of a quantum state from one location to another without physical movement, considering the principles of quantum mechanics such as superposition and entanglement.
"""

def quantum_teleportation(message, alice_epr, alice_measurement, bob_epr):
    # Alice's encoding
    if alice_measurement == 0:
        encoded_message = message
    elif alice_measurement == 1:
        encoded_message = message * -1
    elif alice_measurement == 2:
        encoded_message = message * 1j
    else:
        encoded_message = message * -1j

    # Teleportation
    bob_message = encoded_message * bob_epr

    return bob_message