"""
QUESTION:
Create a function `calculate_molar_mass(rna_sequence)` that takes a string of RNA nucleotides ('A', 'U', 'C', 'G') as input and returns the total molar mass of the sequence. The molar masses of the nucleotides are approximately: 'A' = 347.2212 g/mol, 'U' = 324.1813 g/mol, 'C' = 323.1965 g/mol, and 'G' = 363.2206 g/mol. The function should return the total molar mass rounded to four decimal places.
"""

def calculate_molar_mass(rna_sequence):
    # The molar mass of each nucleotide (in g/mol)
    molar_masses = {
        'A': 347.2212,
        'U': 324.1813,
        'C': 323.1965,
        'G': 363.2206
    }

    # Initialize the total molar mass
    total_molar_mass = 0

    # Add the molar mass of each nucleotide in the sequence
    for nucleotide in rna_sequence:
        total_molar_mass += molar_masses[nucleotide]

    # Return the total molar mass rounded to four decimal places
    return round(total_molar_mass, 4)