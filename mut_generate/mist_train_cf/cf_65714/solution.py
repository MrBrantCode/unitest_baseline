"""
QUESTION:
Create a function called `RNA_Molecular_Weight` that calculates the molecular weight of a given RNA sequence. The function should take an RNA sequence as input, where the sequence consists of the characters 'A', 'U', 'C', and 'G', each representing a nucleotide. The molecular weights of the nucleotides are: 'A' (347.2212), 'U' (324.1813), 'C' (323.1965), and 'G' (363.2206). The function should return the total molecular weight of the RNA sequence.
"""

def RNA_Molecular_Weight(RNA):
    """
    Calculate the molecular weight of a given RNA sequence.

    Args:
    RNA (str): The RNA sequence consisting of the characters 'A', 'U', 'C', and 'G'.

    Returns:
    float: The total molecular weight of the RNA sequence.
    """
    MW = {'A': 347.2212, 'U': 324.1813, 'C': 323.1965, 'G': 363.2206} # Molar mass of each nucleotide
    RNA_MW = 0
    for nucleotide in RNA:
        RNA_MW += MW[nucleotide]
    return RNA_MW