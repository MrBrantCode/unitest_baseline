"""
QUESTION:
Create a function named `generate_subsets` that generates all subsets of a given set, where each subset must contain at least one element from the original set. The function should take a set `input_set` as input and return a list of all subsets. The subsets can be in any order and do not need to be sorted. The function should be able to handle input sets of any size and should not have any constraints on the size of the subsets.
"""

def generate_subsets(input_set):
    subsets = [[]]  # start with an empty subset
    
    for num in input_set:
        new_subsets = []
        for subset in subsets:
            new_subset = subset + [num]
            new_subsets.append(new_subset)
        subsets += new_subsets
    
    # remove empty subset from the list of subsets
    subsets = [subset for subset in subsets if subset]
    
    return subsets