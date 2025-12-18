"""
QUESTION:
Write a function `solve_problem` that takes a list of integers `n` and an integer `count` as input. The function should return all unique sequences of four integers from the list `n` that multiply together to give the `count`. Assume that the list `n` has at least four elements and the `count` is a non-negative integer.
"""

import itertools

def solve_problem(n, count):
    # generate all possible combinations of 4 elements
    all_combinations = list(itertools.combinations(n, 4))

    # initialize a list to store all sequences that match the count
    sequences = []

    # iterate over all combinations
    for comb in all_combinations:
        # compute the product of elements in the current combination
        prod = 1
        for val in comb:
            prod *= val

        # if the product equals the count, add the combination to the sequences list
        if prod == count:
            sequences.append(comb)

    return sequences