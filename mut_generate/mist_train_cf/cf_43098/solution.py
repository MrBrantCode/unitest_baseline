"""
QUESTION:
Create a function `calculate_atom_distance(geometry_data, atom_index1, atom_index2)` that calculates the Euclidean distance between two atoms in a molecule given their indices. The function takes a list of tuples `geometry_data` as input, where each tuple contains an atomic symbol and 3D coordinates (x, y, z). The indices `atom_index1` and `atom_index2` are 0-based and correspond to the atoms for which the distance needs to be calculated. The input geometry data is guaranteed to be valid and contain at least two atoms.
"""

import math

def calculate_atom_distance(geometry_data, atom_index1, atom_index2):
    atom1_coords = geometry_data[atom_index1][1]
    atom2_coords = geometry_data[atom_index2][1]
    
    distance = math.sqrt((atom2_coords[0] - atom1_coords[0])**2 + 
                         (atom2_coords[1] - atom1_coords[1])**2 + 
                         (atom2_coords[2] - atom1_coords[2])**2)
    
    return distance