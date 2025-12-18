"""
QUESTION:
Create a function called `reverse_complement` that takes a DNA string as input and returns its reverse complement. The function must be implemented using only bitwise operations and a constant amount of extra space. The reverse complement of a DNA string is formed by reversing the string and then replacing each nucleotide with its complement (A → T, C → G). The function should have a time complexity of O(n), where n is the length of the input string, and a space complexity of O(1).
"""

def reverse_complement(dna):
    complements = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(complements[base] for base in dna[::-1])