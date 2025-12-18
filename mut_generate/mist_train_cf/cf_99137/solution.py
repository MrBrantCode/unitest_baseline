"""
QUESTION:
Develop a Python function `oxygen_distribution` that calculates the average oxygen atom distribution across multiple flakes of graphene oxide. The function should take a list of tuples as input, where each tuple contains the number of carbon, hydrogen, and oxygen atoms in a flake, and return the average distribution of oxygen atoms.
"""

def oxygen_distribution(flakes):
    total_oxygen = 0
    for flake in flakes:
        c, h, o = flake
        total_atoms = c + h + o
        oxygen = o / total_atoms
        total_oxygen += oxygen
    average_oxygen = total_oxygen / len(flakes)
    return average_oxygen