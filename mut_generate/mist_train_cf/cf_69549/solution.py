"""
QUESTION:
Write a function `all_feasible_sequences(lst, target)` that takes a list of integers `lst` and a target integer `target` as input, and returns all feasible sequences of digits in `lst` that create a product equivalent to `target`. The function should consider all possible combinations of digits in `lst` and return the combinations whose product equals `target`.
"""

import itertools

def all_feasible_sequences(lst, target):
    feasible_sequences = []
    for r in range(1, len(lst)+1):
        # Generate all combinations of r elements
        combinations = list(itertools.combinations(lst, r))
        # calculate product for each combination 
        for comb in combinations:
            product = 1
            for num in comb:
                product *= num
            # if the product equals to target, then we found a feasible sequence
            if product == target:
                feasible_sequences.append(comb)

    return feasible_sequences