"""
QUESTION:
Create a function named `generate_strings` that takes an integer `k` as input and returns all unique combinations of strings with a length of `k` using the characters 'a', 'b', 'c', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'. The function should exclude any combinations containing the sequences 'abc' or '123'. The function should be able to handle large values of `k`.
"""

import itertools

def generate_strings(k):
    set_values = {'a', 'b', 'c', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9'}
    result = []
    for p in itertools.product(set_values, repeat=k):
        string_comb = ''.join(p)
        if 'abc' not in string_comb and '123' not in string_comb:
            result.append(string_comb)
    return result