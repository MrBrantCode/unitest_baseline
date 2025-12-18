"""
QUESTION:
Create a function `calculate_rna_mass` that takes a string of RNA nucleotides as input and returns the approximate monomeric mass of the RNA chain in g/mol. The RNA nucleotides and their corresponding monomeric weights are: Adenine (A) - 347.2 g/mol, Uracil (U) - 324.2 g/mol, Cytosine (C) - 323.2 g/mol, and Guanine (G) - 363.2 g/mol. The function should return an error message and terminate if any invalid nucleotide is encountered.
"""

def calculate_rna_mass(rna_sequence):
    # Defining the monomeric weight of each RNA nucleotide
    rna_weights = {
      'A': 347.2,
      'U': 324.2,
      'C': 323.2,
      'G': 363.2
    }
    rna_mass = 0
    for nucleotide in rna_sequence:
        if nucleotide in rna_weights.keys():
            rna_mass += rna_weights[nucleotide]
        else:
            print("Invalid nucleotide detected!")
            return
    return rna_mass