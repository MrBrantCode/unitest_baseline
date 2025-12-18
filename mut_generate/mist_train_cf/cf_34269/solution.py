"""
QUESTION:
Apply the fixed modifications to the N-terminus of a protein sequence. 

Write a function `apply_fixed_modifications` that takes a protein sequence and a dictionary of fixed modifications as input and returns the modified protein sequence as a string. The dictionary keys are integers representing the position of the modification within the protein sequence (0 for N-terminus), and the values are lists of Modification objects with a Description property. The function should apply the fixed modifications at position 0 to the protein sequence and return the modified sequence.
"""

class Modification:
    def __init__(self, description):
        self.Description = description

def apply_fixed_modifications(protein_sequence, fixed_modifications):
    modified_sequence = protein_sequence
    if 0 in fixed_modifications:
        prot_n_term_fixed_mods = fixed_modifications[0]
        for fixed_modification in prot_n_term_fixed_mods:
            modified_sequence = f"[{fixed_modification.Description}]{modified_sequence}"
    return modified_sequence