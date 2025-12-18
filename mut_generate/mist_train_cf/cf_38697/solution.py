"""
QUESTION:
Implement the `generate_unique_test_case` function, which takes in two parameters: `minLength` and `minSequences`. It should return a list of `minSequences` number of unique sequences, each of length `minLength`, where each sequence is a tuple of digits from 0 to 9. Ensure that no sequence is a duplicate of a previously generated one, and also no sequence is a larger version of a previously generated one (i.e., it does not have a common prefix with any previously generated sequence).
"""

import itertools

def generate_unique_test_case(minLength, minSequences):
    generated_test_cases = set()

    all_combinations = list(itertools.product(range(10), repeat=minLength))
    unique_test_cases = [seq for seq in all_combinations 
                         if seq not in generated_test_cases and 
                         all(seq != existing[:len(seq)] for existing in generated_test_cases)]
    selected_test_cases = unique_test_cases[:minSequences]
    generated_test_cases.update(selected_test_cases)

    return selected_test_cases