"""
QUESTION:
Create a function `find_combinations(tuples_list, target)` that takes a list of tuples and a target value as input parameters. The function should return all combinations of the second elements of tuples where the sum of their first elements equals the target value. The tuples list and the target value are non-negative integers, and the function should return all possible combinations without any specific order.
"""

import itertools

def find_combinations(tuples_list, target):
    result = []
    for r in range(1, len(tuples_list)+1):
        for combination in itertools.combinations(tuples_list, r):
            if sum(x[0] for x in combination) == target:
                result.append(tuple(x[1] for x in combination))
    return result