"""
QUESTION:
Write a function `generate_powerset(s)` that generates the powerset of a given set `s` without using recursion, with a time complexity of O(2^N), where N is the length of the input set. The function should take an iterable `s` as input and return a list of lists, where each sublist is a subset of `s`.
"""

def generate_powerset(s):
    powerset = [[]]  # Initialize the powerset with an empty set
    for elem in s:
        # For each element in the input set, add it to all existing subsets
        new_subsets = []
        for subset in powerset:
            new_subsets.append(subset + [elem])
        powerset.extend(new_subsets)
    return powerset