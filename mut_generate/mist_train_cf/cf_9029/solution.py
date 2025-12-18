"""
QUESTION:
Write a function `powerset_with_duplicates` that generates the powerset of a given list, preserving any duplicate elements in the original list. The function should return a list of lists, where each sublist is a unique subset of the original list.
"""

def powerset_with_duplicates(lst):
    powerset = [[]]
    for num in lst:
        new_subsets = []
        for subset in powerset:
            new_subset = subset + [num]
            new_subsets.append(new_subset)
        powerset += new_subsets
    return powerset