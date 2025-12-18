"""
QUESTION:
Write a function called `calculate_transverse_strain` that takes the Poisson's ratio (`nu`) and axial strain (`epsilon_a`) as input and returns the transverse strain (`epsilon_t`). Assume that the Poisson's ratio and axial strain are given as floating-point numbers. The function should not take any other arguments.
"""

def calculate_transverse_strain(nu, epsilon_a):
    """
    Calculate the transverse strain (epsilon_t) given Poisson's ratio (nu) and axial strain (epsilon_a).

    Args:
        nu (float): Poisson's ratio.
        epsilon_a (float): Axial strain.

    Returns:
        float: Transverse strain.
    """
    return -nu * epsilon_a