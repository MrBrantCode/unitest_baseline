"""
QUESTION:
Create a function `generate_subsets` that takes a set of elements as input and returns a list of all possible subsets. The function should not take any additional parameters and the input set should not be modified. The output list should include the empty set and the set itself.
"""

def generate_subsets(elements):
    subsets = [[]]
    for element in elements:
        subsets += [subset + [element] for subset in subsets]
    return subsets