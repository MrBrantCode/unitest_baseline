"""
QUESTION:
You are a biologist working on the amino acid  composition of proteins. Every protein consists of a long chain of 20 different amino acids with different properties. 
Currently, you are collecting data on the percentage, various amino acids make up a protein you are working on. As manually counting the occurences of amino acids takes too long (especially when counting more than one amino acid), you decide to write a program for this task:

Write a function that takes two arguments,
 1. A (snippet of a) protein sequence
 2. A list of amino acid residue codes 

and returns the rounded percentage of the protein that the given amino acids make up. 
If no amino acid list is given, return the percentage of hydrophobic amino acid residues ["A", "I", "L", "M", "F", "W", "Y", "V"].
"""

def calculate_amino_acid_percentage(protein_sequence, amino_acid_residues=['A', 'I', 'L', 'M', 'F', 'W', 'Y', 'V']):
    return round(sum((protein_sequence.count(r) for r in amino_acid_residues)) / len(protein_sequence) * 100)