"""
QUESTION:
Implement a function `quantum_entanglement(n, particles)` that simulates quantum entanglement between `n` particles and returns the entangled state. The function should take an integer `n` as input, representing the number of particles, and a list of `particles` representing the initial state of each particle. The function should return the entangled state of the particles.
"""

def quantum_entanglement(n, particles):
    entangled_state = []
    for i in range(2**n):
        state = []
        for j in range(n):
            state.append(particles[j] if (i & (1 << j)) else 0)
        entangled_state.append(state)
    return entangled_state