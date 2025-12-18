"""
QUESTION:
Create a function named `convert_to_amino_acids` that takes a DNA sequence as input, converts it into its corresponding amino acid sequence using the provided codon table, and returns the amino acid sequence. The DNA sequence is a valid sequence of nucleotides (A, T, C, G) and its length is a multiple of 3. The codon table maps each codon (a sequence of three DNA nucleotides) to its corresponding amino acid.

The codon table is as follows:
```
Isoleucine    ATT ATC ATA
Leucine       CTT CTC CTA CTG TTA TTG
Valine        GTT GTC GTA GTG
Phenylalanine TTT TTC
Methionine    ATG
Cysteine      TGT TGC
Alanine       GCT GCC GCA GCG
```
"""

def convert_to_amino_acids(dna_sequence):
    codon_table = {
        'ATT': 'Isoleucine', 'ATC': 'Isoleucine', 'ATA': 'Isoleucine',
        'CTT': 'Leucine', 'CTC': 'Leucine', 'CTA': 'Leucine', 'CTG': 'Leucine', 'TTA': 'Leucine', 'TTG': 'Leucine',
        'GTT': 'Valine', 'GTC': 'Valine', 'GTA': 'Valine', 'GTG': 'Valine',
        'TTT': 'Phenylalanine', 'TTC': 'Phenylalanine',
        'ATG': 'Methionine',
        'TGT': 'Cysteine', 'TGC': 'Cysteine',
        'GCT': 'Alanine', 'GCC': 'Alanine', 'GCA': 'Alanine', 'GCG': 'Alanine'
    }
    amino_acids = []
    for i in range(0, len(dna_sequence), 3):
        codon = dna_sequence[i:i+3]
        amino_acid = codon_table.get(codon, 'Unknown')
        amino_acids.append(amino_acid)
    return ''.join(amino_acids)