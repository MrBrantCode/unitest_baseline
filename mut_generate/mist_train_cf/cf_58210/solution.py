"""
QUESTION:
Develop a program that takes a given RNA sequence as input and performs the following tasks: 

1. Validates the RNA sequence by ensuring it only contains valid RNA nucleotides (A, U, C, G). 
2. Estimates the molecular weight of the RNA sequence using the average molecular weights of A (347.2), C (323.2), G (363.2), and U (324.2).
3. Calculates the percentage composition of each nucleotide type in the RNA sequence.

The program should include error handling for invalid RNA sequences and should use the following function names: 
- validate(seq) for validating the RNA sequence
- molecular_weight(seq) for calculating the molecular weight
- composition(seq) for calculating the percentage composition.
"""

# Function to validate RNA sequence
def validate(seq):
    valid_nucleotides = set(['A', 'C', 'G', 'U'])
    for nucleotide in seq:
        if nucleotide not in valid_nucleotides:
            return False
    return True

# Function to estimate molecular weight
def molecular_weight(seq):
    weight_dict = {"A": 347.2, "C": 323.2, "G": 363.2, "U": 324.2}
    weight = sum(weight_dict[i] for i in seq)
    return weight

# Function to calculate percentage composition
def composition(seq):
    comp_dict = {"A": 0, "C": 0, "G": 0, "U": 0}
    for nucleotide in seq:
        comp_dict[nucleotide] += 1
    for key, value in comp_dict.items():
        comp_dict[key] = (value / len(seq)) * 100
    return comp_dict