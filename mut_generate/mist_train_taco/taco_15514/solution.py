"""
QUESTION:
In genetic the reverse complement of a sequence is formed by **reversing** the sequence and then taking the complement of each symbol.

The four nucleotides in DNA is Adenine (A), Cytosine (C), Guanine (G) and Thymine (Thymine). 

- A is the complement of T 
- C is the complement of G.

This is a bi-directional relation so:

- T is the complement of A
- G is the complement of C.

For this kata you need to complete the reverse complement function that take a DNA string and return the reverse complement string.

**Note**: You need to take care of lower and upper case. And if a sequence conatains some invalid characters you need to return "Invalid sequence".

This kata is based on the following [one](http://www.codewars.com/kata/complementary-dna/ruby) but with a little step in addition.
"""

def reverse_complement(dna: str) -> str:
    # Define the complement mapping
    complement_map = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C',
                      'a': 't', 't': 'a', 'c': 'g', 'g': 'c'}
    
    try:
        # Reverse the sequence and get the complement of each nucleotide
        reverse_comp = ''.join(complement_map[nucleotide] for nucleotide in reversed(dna))
        return reverse_comp
    except KeyError:
        # If any invalid character is found, return "Invalid sequence"
        return "Invalid sequence"