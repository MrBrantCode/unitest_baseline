"""
QUESTION:
Write a function `calculate_distance` that takes a list of strings `coordinates` representing the coordinates of atoms in a molecular structure, and two strings `atom1` and `atom2` representing the symbols of the two atoms for which the distance needs to be calculated.

`coordinates` is a list of strings where each string contains an atom's symbol followed by its x, y, and z coordinates separated by spaces. The coordinates are given in Cartesian space and are represented as floating-point numbers. The atom symbols are case-sensitive.

The function should return the distance between `atom1` and `atom2` as a floating-point number rounded to 4 decimal places if both `atom1` and `atom2` are present in the input coordinates. If either `atom1` or `atom2` is not present in the input coordinates, the function should return the string "Invalid atom symbol". The distance is calculated using the Euclidean distance formula: Distance = sqrt((x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2).
"""

def calculate_distance(coordinates, atom1, atom2):
    atom_coords = {}
    for coord in coordinates:
        atom, x, y, z = coord.split()
        atom_coords[atom] = (float(x), float(y), float(z))

    if atom1 not in atom_coords or atom2 not in atom_coords:
        return "Invalid atom symbol"
    
    x1, y1, z1 = atom_coords[atom1]
    x2, y2, z2 = atom_coords[atom2]

    distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2) ** 0.5
    return round(distance, 4)