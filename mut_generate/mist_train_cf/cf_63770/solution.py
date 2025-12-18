"""
QUESTION:
Write a function `entangled_particles` that takes a list of particles and returns a list of tuples representing the entangled particles and their respective states.
"""

def entangled_particles(particles):
    entangled = []
    for i in range(0, len(particles), 2):
        if i + 1 < len(particles):
            entangled.append((particles[i], particles[i + 1]))
    return entangled