"""
QUESTION:
Write a function `construct_lattice` that constructs a lattice from a set of basis vectors. The function should take as input a list of basis vectors and return a lattice object that can be used to perform various lattice operations. The lattice object should have the following properties: it should be a regular, infinite arrangement of points in space, each of which is an integer linear combination of the basis vectors.
"""

import numpy as np

class Lattice:
    def __init__(self, basis_vectors):
        self.basis_vectors = np.array(basis_vectors)

    def __str__(self):
        return f'Lattice with basis vectors:\n{self.basis_vectors}'

def construct_lattice(basis_vectors):
    return Lattice(basis_vectors)