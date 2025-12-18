"""
QUESTION:
Create a function called `replicate_dna` that simulates the process of DNA replication. The function should take a DNA sequence of length 10, consisting of the nucleotides A, T, C, and G, and return the replicated DNA strand. The replication process should be visualized using a replication fork, and the enzymes helicase and DNA polymerase, as well as the key proteins sliding clamp and topoisomerase, should be included in the simulation.
"""

def replicate_dna(original_strand):
    # Define the complementary base pairs
    base_pairs = {
        "A": "T",
        "T": "A",
        "C": "G",
        "G": "C"
    }
    # Create the complementary DNA strand
    complementary_strand = "".join(base_pairs[nucleotide] for nucleotide in original_strand)
    # Return the replicated DNA strand
    return original_strand + complementary_strand