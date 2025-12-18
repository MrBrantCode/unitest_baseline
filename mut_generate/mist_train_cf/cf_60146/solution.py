"""
QUESTION:
Create a function called `quantum_key_distribution` that demonstrates a simplified Quantum Key Distribution (QKD) protocol, highlighting its basic principles and security measures. This function should not implement the full complexity of QKD protocols, but rather provide a general understanding of the technique.
"""

def quantum_key_distribution(alice_bits, alice_bases, bob_bases):
    shared_key = []
    for alice_bit, alice_base, bob_base in zip(alice_bits, alice_bases, bob_bases):
        if alice_base == bob_base:
            shared_key.append(alice_bit)
    return shared_key