"""
QUESTION:
Create a function named `coulomb_matrix` that takes in two parameters: `charges` and `positions`. `charges` is a list of atomic charges in atomic units and `positions` is a 2D numpy array representing the positions of the atoms in 3D space in Angstroms. The function should return the Coulomb matrix for the given atoms. The Coulomb matrix is a square matrix where the element at the i-th row and j-th column is calculated as `Z_i * Z_j / |r_i - r_j|` if `i` is not equal to `j`, and `0` otherwise, where `Z_i` and `Z_j` are the atomic charges of atoms `i` and `j`, and `r_i` and `r_j` are their positions in 3D space.
"""

import numpy as np

def coulomb_matrix(charges, positions):
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