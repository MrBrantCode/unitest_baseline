"""
QUESTION:
Write a function `dna_rna_composition` that takes a DNA sequence as input and returns the estimated atomic composition of the DNA sequence, the corresponding RNA strand, and its estimated atomic composition. The function should consider nucleotide pairing and replace 'T' with 'U' in the RNA strand. The atomic composition of each nucleotide is represented as ['Chemical_name', 'Chemical_formula']. The input DNA sequence will consist of the characters 'A', 'C', 'G', and 'T'.
"""

def dna_rna_composition(DNA):
    atomic_compositions = {
        'A': ['Adenine', 'C5H5N5'],
        'T': ['Thymine', 'C5H6N2O2'],
        'C': ['Cytosine', 'C4H5N3O'],
        'G': ['Guanine', 'C5H5N5O'],
        'U': ['Uracil', 'C4H4N2O2'] 
    }

    DNA_atomic_comp = []
    RNA_atomic_comp = []
    RNA_strand = ""
    
    for nucleotide in DNA:
        DNA_atomic_comp.append(atomic_compositions[nucleotide])
        if nucleotide == 'T':
            RNA_strand += 'U'
            RNA_atomic_comp.append(atomic_compositions['U'])
        else:
            RNA_strand += nucleotide
            RNA_atomic_comp.append(atomic_compositions[nucleotide])
    
    return DNA_atomic_comp, RNA_strand, RNA_atomic_comp