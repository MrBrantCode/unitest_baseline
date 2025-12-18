"""
QUESTION:
Write a function `all_subsets(input_set)` to generate all possible subsets of a given input set. The function should take a set `input_set` as input and return a list of all subsets, including the empty set and the input set itself. The subsets should be represented as lists.
"""

def all_subsets(input_set):
    res = [[]]
    for ele in input_set:
        res += [i + [ele] for i in res]
    return res