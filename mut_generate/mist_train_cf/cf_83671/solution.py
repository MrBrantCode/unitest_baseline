"""
QUESTION:
Given the quantum entanglement state, a pair of particles represented as a dictionary where each key is a particle ID and the value is a list of states it can have, implement a function `generate_entangled_state` that takes in the number of particles and the possible states each particle can have, and returns the entangled state of the particles as a dictionary.
"""

def generate_entangled_state(num_particles, states):
    """
    Generate the entangled state of particles.

    Args:
    num_particles (int): The number of particles.
    states (list): A list of possible states each particle can have.

    Returns:
    dict: A dictionary representing the entangled state of particles.
    """
    entangled_state = {}
    for i in range(num_particles):
        entangled_state[i] = states
    return entangled_state