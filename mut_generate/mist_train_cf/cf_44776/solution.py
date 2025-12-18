"""
QUESTION:
Write a function called `is_entangled` that determines whether two particles are entangled based on their spin properties. Assume the spin of a particle can be either 'up' or 'down'. Two particles are considered entangled if their spins are correlated such that the spin of one particle is always the opposite of the spin of the other particle.
"""

def is_entangled(particle1, particle2):
    """
    Determine whether two particles are entangled based on their spin properties.

    Args:
        particle1 (dict): The spin properties of the first particle.
        particle2 (dict): The spin properties of the second particle.

    Returns:
        bool: True if the particles are entangled, False otherwise.
    """
    return particle1['spin'] != particle2['spin']