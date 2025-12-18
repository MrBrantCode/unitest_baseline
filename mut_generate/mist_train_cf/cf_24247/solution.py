"""
QUESTION:
Write a function `find_subsets` that generates all possible subsets of a given set. The function should take a set of elements as input and return all possible subsets of that set.
"""

def find_subsets(s):
    subsets = []
    for r in range(len(s) + 1):
        subsets.extend(itertools.combinations(s, r))
    return subsets