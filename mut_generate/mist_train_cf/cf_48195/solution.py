"""
QUESTION:
Create a Python function `generate_permutations(input_set, k)` that generates every distinct permutation of strings with a length of `k` using the provided lowercase alphabet characters in `input_set`. 

The function should produce all unique combinations of the characters in `input_set` and the length of each combination should be `k`. Also, implement another function `encode_base64(input_strings)` that accepts the generated strings and encodes them using Base64. 

The function should return a list of encoded strings. Assume that the input set only contains lowercase alphabet characters and `k` is a positive integer.
"""

import itertools
import base64

def generate_permutations(input_set, k):
    """Generate all distinct permutations of strings with a length of k"""
    # Convert the set to a list
    input_list = list(input_set)
    
    # Generate all permutations of length k
    permutations = list(itertools.product(input_list, repeat=k))
    
    # Convert the permutations to strings
    permutations = [''.join(p) for p in permutations]
    
    return permutations

def encode_base64(input_strings):
    """Encode the input strings using Base64"""
    # Encode each string and store it in a new list
    encoded_strings = [base64.b64encode(s.encode()).decode() for s in input_strings]
    
    return encoded_strings