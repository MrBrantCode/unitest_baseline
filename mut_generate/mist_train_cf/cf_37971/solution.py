"""
QUESTION:
Write a function `count_atoms_in_supercell` that calculates the total number of atoms in a supercell. The function should take three parameters: `unitcell_lattice`, a 3x3 matrix representing the lattice vectors of the unit cell; `unitcell_atoms`, a list of atomic positions in the unit cell; and `supercell_matrix`, a 3x3 matrix that defines how many times the unit cell is repeated in each direction to form the supercell. The function should return the total number of atoms in the supercell. The input matrices are 3x3 and the atomic positions are 3D coordinates.
"""

import numpy as np

def count_atoms_in_supercell(unitcell_lattice, unitcell_atoms, supercell_matrix):
    unitcell_lattice = np.array(unitcell_lattice)
    unitcell_atoms = np.array(unitcell_atoms)
    total_atoms_unitcell = len(unitcell_atoms)
    volume_scaling_factor = abs(np.linalg.det(supercell_matrix))
    total_atoms_supercell = int(total_atoms_unitcell * volume_scaling_factor)
    return total_atoms_supercell