"""
QUESTION:
Write a function `calculate_coulomb_matrix` that calculates the Coulomb matrix elements for a system of atoms. The function should take in two inputs: `charges`, a list of atomic charges, and `positions`, a 2D NumPy array of atomic positions. The function should return a 2D NumPy array representing the Coulomb matrix.
"""

import numpy as np

def calculate_coulomb_matrix(charges, positions):
    n_atoms = len(charges)
    coulomb_matrix = np.zeros((n_atoms, n_atoms))
    for i in range(n_atoms):
        for j in range(n_atoms):
            if i == j:
                coulomb_matrix[i, j] = 0
            else:
                distance = np.linalg.norm(positions[i] - positions[j])
                coulomb_matrix[i, j] = charges[i] * charges[j] / distance
    return coulomb_matrix