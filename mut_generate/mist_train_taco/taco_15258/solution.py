"""
QUESTION:
Our cells go through a process called protein synthesis to translate the instructions in DNA into an amino acid chain, or polypeptide.

Your job is to replicate this!

---

**Step 1: Transcription**

Your input will be a string of DNA that looks like this:

`"TACAGCTCGCTATGAATC"`


You then must transcribe it to mRNA. Each letter, or base, gets transcribed.


```T -> A
A -> U
G -> C
C -> G```

Also, you will split it into groups of three, or _codons_.

The above example would become:

`"AUG UCG AGC GAU ACU UAG"`

---

**Step 2: Translation**

After you have the mRNA strand, you will turn it into an amino acid chain.

Each codon corresponds to an amino acid:

```
Ala     GCU, GCC, GCA, GCG
Leu     UUA, UUG, CUU, CUC, CUA, CUG
Arg     CGU, CGC, CGA, CGG, AGA, AGG
Lys     AAA, AAG
Asn     AAU, AAC
Met     AUG
Asp     GAU, GAC
Phe     UUU, UUC
Cys     UGU, UGC
Pro     CCU, CCC, CCA, CCG
Gln     CAA, CAG
Ser     UCU, UCC, UCA, UCG, AGU, AGC
Glu     GAA, GAG
Thr     ACU, ACC, ACA, ACG
Gly     GGU, GGC, GGA, GGG
Trp     UGG
His     CAU, CAC
Tyr     UAU, UAC
Ile     AUU, AUC, AUA
Val     GUU, GUC, GUA, GUG
Stop   UAG, UGA, UAA```

Phew, that's a long list!

The above example would become:

`"Met Ser Ser Thr Asp Stop"`

Any additional sets of bases that aren't in a group of three aren't included. For example:

`"AUG C"`

would become

`"Met"`

---

Anyway, your final output will be the mRNA sequence and the polypeptide.

Here are some examples:

*In:*

`"TACAGCTCGCTATGAATC"`

*Out:*

`["AUG UCG AGC GAU ACU UAG","Met Ser Ser Asp Thr Stop"]`

---

*In:*

`"ACGTG"`

*Out:*

`["UGC AC","Cys"]`
"""

import re

# Translation table for DNA to mRNA
TABLE = str.maketrans('ACGT', 'UGCA')

# Codon to Amino Acid dictionary
CODON_DICT = {
    'GCU': 'Ala', 'GCC': 'Ala', 'GCA': 'Ala', 'GCG': 'Ala',
    'UUA': 'Leu', 'UUG': 'Leu', 'CUU': 'Leu', 'CUC': 'Leu', 'CUA': 'Leu', 'CUG': 'Leu',
    'CGU': 'Arg', 'CGC': 'Arg', 'CGA': 'Arg', 'CGG': 'Arg', 'AGA': 'Arg', 'AGG': 'Arg',
    'AAA': 'Lys', 'AAG': 'Lys',
    'AAU': 'Asn', 'AAC': 'Asn',
    'AUG': 'Met',
    'GAU': 'Asp', 'GAC': 'Asp',
    'UUU': 'Phe', 'UUC': 'Phe',
    'UGU': 'Cys', 'UGC': 'Cys',
    'CCU': 'Pro', 'CCC': 'Pro', 'CCA': 'Pro', 'CCG': 'Pro',
    'CAA': 'Gln', 'CAG': 'Gln',
    'UCU': 'Ser', 'UCC': 'Ser', 'UCA': 'Ser', 'UCG': 'Ser', 'AGU': 'Ser', 'AGC': 'Ser',
    'GAA': 'Glu', 'GAG': 'Glu',
    'ACU': 'Thr', 'ACC': 'Thr', 'ACA': 'Thr', 'ACG': 'Thr',
    'GGU': 'Gly', 'GGC': 'Gly', 'GGA': 'Gly', 'GGG': 'Gly',
    'UGG': 'Trp',
    'CAU': 'His', 'CAC': 'His',
    'UAU': 'Tyr', 'UAC': 'Tyr',
    'AUU': 'Ile', 'AUC': 'Ile', 'AUA': 'Ile',
    'GUU': 'Val', 'GUC': 'Val', 'GUA': 'Val', 'GUG': 'Val',
    'UAG': 'Stop', 'UGA': 'Stop', 'UAA': 'Stop'
}

def transcribe_and_translate(dna):
    # Step 1: Transcribe DNA to mRNA
    rna = dna.translate(TABLE)
    
    # Step 2: Split mRNA into codons
    codons = re.findall('.{1,3}', rna)
    
    # Step 3: Translate codons to amino acids
    amino_acids = [CODON_DICT.get(codon, '') for codon in codons]
    
    # Step 4: Filter out any empty strings from incomplete codons
    amino_acids = [aa for aa in amino_acids if aa]
    
    # Step 5: Join codons and amino acids into space-separated strings
    rna_sequence = ' '.join(codons)
    polypeptide_sequence = ' '.join(amino_acids)
    
    return (rna_sequence, polypeptide_sequence)