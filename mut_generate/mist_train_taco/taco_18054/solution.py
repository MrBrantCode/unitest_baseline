"""
QUESTION:
In genetics 2 differents DNAs sequences can code for the same protein. 

This is due to the redundancy of the genetic code, in fact 2 different tri-nucleotide can code for the same amino-acid.
For example the tri-nucleotide 'TTT' and the tri-nucleotide 'TTC' both code for the amino-acid 'F'. For more information you can take a look [here](https://en.wikipedia.org/wiki/DNA_codon_table).

Your goal in this kata is to define if two differents DNAs sequences code for exactly the same protein. Your function take the 2 sequences you should compare.
For some kind of simplicity here the sequences will respect the following rules:

- It is a full protein sequence beginning with a Start codon and finishing by an Stop codon
- It will only contain valid tri-nucleotide. 

The translation hash is available for you under a translation hash `$codons` [Ruby] or `codons` [Python and JavaScript].

To better understand this kata you can take a look at this [one](https://www.codewars.com/kata/5708ef48fe2d018413000776), it can help you to start.
"""

def are_sequences_coding_same_protein(seq1, seq2):
    if seq1 == seq2:
        return True
    
    codon_groups = [
        ['GCT', 'GCC', 'GCA', 'GCG'], ['CGT', 'CGC', 'CGA', 'CGG', 'AGA', 'AGG'], 
        ['AAT', 'AAC'], ['GAT', 'GAC'], ['AAT', 'AAC', 'GAT', 'GAC'], ['TGT', 'TGC'], 
        ['CAA', 'CAG'], ['GAA', 'GAG'], ['CAA', 'CAG', 'GAA', 'GAG'], ['GGT', 'GGC', 'GGA', 'GGG'], 
        ['CAT', 'CAC'], ['ATG'], ['ATT', 'ATC', 'ATA'], ['CTT', 'CTC', 'CTA', 'CTG', 'TTA', 'TTG'], 
        ['AAA', 'AAG'], ['ATG'], ['TTT', 'TTC'], ['CCT', 'CCC', 'CCA', 'CCG'], 
        ['TCT', 'TCC', 'TCA', 'TCG', 'AGT', 'AGC'], ['ACT', 'ACC', 'ACA', 'ACG'], ['TGG'], 
        ['TAT', 'TAC'], ['GTT', 'GTC', 'GTA', 'GTG'], ['TAA', 'TGA', 'TAG']
    ]
    
    for group in codon_groups:
        for i in range(0, len(seq1), 3):
            if seq1[i:i + 3] in group and seq2[i:i + 3] not in group:
                return False
    
    return True