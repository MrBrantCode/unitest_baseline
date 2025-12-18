"""
QUESTION:
Implement a function named `genetic_code_generator` that takes a list of DNA nucleotides as input and returns a list of corresponding genetic codes. The input list can contain the following DNA nucleotides: A, C, G, and T. The genetic codes are the amino acids corresponding to the sequence of DNA nucleotides. The genetic codes should be represented as a list of strings, where each string is one of the 20 amino acid names.
"""

def genetic_code_generator(dna_nucleotides):
    """
    Generate a list of genetic codes from a given list of DNA nucleotides.

    Args:
        dna_nucleotides (list): A list of DNA nucleotides.

    Returns:
        list: A list of corresponding genetic codes.

    """
    genetic_code_map = {
        'ATA': 'I', 'ATC': 'I', 'ATT': 'I', 'ATG': 'M',
        'ACA': 'T', 'ACC': 'T', 'ACG': 'T', 'ACT': 'T',
        'AAC': 'N', 'AAT': 'N', 'AAA': 'K', 'AAG': 'K',
        'AGC': 'S', 'AGT': 'S', 'AGA': 'R', 'AGG': 'R',
        'CTA': 'L', 'CTC': 'L', 'CTG': 'L', 'CTT': 'L',
        'CCA': 'P', 'CCC': 'P', 'CCG': 'P', 'CCT': 'P',
        'CAC': 'H', 'CAT': 'H', 'CAA': 'Q', 'CAG': 'Q',
        'CGA': 'R', 'CGC': 'R', 'CGG': 'R', 'CGT': 'R',
        'GTA': 'V', 'GTC': 'V', 'GTG': 'V', 'GTT': 'V',
        'GCA': 'A', 'GCC': 'A', 'GCG': 'A', 'GCT': 'A',
        'GAC': 'D', 'GAT': 'D', 'GAA': 'E', 'GAG': 'E',
        'GGA': 'G', 'GGC': 'G', 'GGG': 'G', 'GGT': 'G',
        'TCA': 'S', 'TCC': 'S', 'TCG': 'S', 'TCT': 'S',
        'TTC': 'F', 'TTT': 'F', 'TTA': 'L', 'TTG': 'L',
        'TAC': 'Y', 'TAT': 'Y', 'TAA': '*', 'TAG': '*',
        'TGC': 'C', 'TGT': 'C', 'TGA': '*', 'TGG': 'W',
    }

    genetic_codes = []
    for i in range(0, len(dna_nucleotides), 3):
        codon = ''.join(dna_nucleotides[i:i+3])
        genetic_codes.append(genetic_code_map.get(codon, 'X'))

    return genetic_codes