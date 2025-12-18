"""
QUESTION:
Write a function `quantum_entanglement` to calculate and return the number of particles that can be entangled in a quantum system given the number of particles and the maximum entanglement level. The function should take two parameters: `num_particles` and `max_entanglement_level`. The function should return the total number of entangled particles. Note that a particle can only be entangled with another particle that has at most one more entanglement level.
"""

def quantum_entanglement(num_particles, max_entanglement_level):
    """
    Calculate the number of particles that can be entangled in a quantum system.

    Parameters:
    num_particles (int): The number of particles in the quantum system.
    max_entanglement_level (int): The maximum entanglement level.

    Returns:
    int: The total number of entangled particles.
    """
    entangled_particles = 0
    for i in range(num_particles):
        for j in range(i + 1, min(i + max_entanglement_level + 1, num_particles)):
            entangled_particles += 1
    return entangled_particles