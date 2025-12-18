"""
QUESTION:
Create a function called `entangled_particles` that takes two particles (A and B) and calculates the state of particle B based on the state of particle A, regardless of the distance between them.
"""

def entangled_particles(particle_A):
    if particle_A == "spin-up":
        return "spin-down"
    elif particle_A == "spin-down":
        return "spin-up"
    else:
        return "Invalid particle state"