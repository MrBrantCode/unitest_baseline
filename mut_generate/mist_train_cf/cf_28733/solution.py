"""
QUESTION:
Create a function `complementary_sequence` that takes a string `dna_sequence` of length 1 to 10^5 containing characters A, T, C, and G, and returns its complementary DNA sequence by pairing A with T and C with G, ignoring any other characters.
"""

def complementary_sequence(dna_sequence):
    sc = ""
    for n in dna_sequence:
        if n == "A":
            sc = sc + "T"
        elif n == "T":
            sc = sc + "A"
        elif n == "C":
            sc = sc + "G"
        elif n == "G":
            sc = sc + "C"
        else:
            continue

    return sc