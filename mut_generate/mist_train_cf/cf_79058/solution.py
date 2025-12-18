"""
QUESTION:
Write a function `generate_subsets(original_set)` that generates all possible subsets of a given set of elements, including the empty set and duplicate subsets of non-distinct elements, with a time complexity below O(2^n * n).
"""

def generate_subsets(original_set):
    subset_list = [[]]
    for ele in original_set:
        subset_list.extend([subset + [ele] for subset in subset_list])
    return subset_list