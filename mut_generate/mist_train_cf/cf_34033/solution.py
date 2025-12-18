"""
QUESTION:
Create a Python class method `possible_usernames` that generates a list of potential usernames. The method should take a format string with a `{permutation}` placeholder and a list of permutations as instance variables. It should replace the placeholder with each permutation in the list and return the resulting list of usernames. The method should be part of a class initialized with a `config` dictionary and a `permutations_list`.
"""

def entance(config, permutations_list):
    possible_usernames = []

    for permutation in permutations_list:
        possible_usernames.append(config['format'].format(permutation=permutation))

    return possible_usernames