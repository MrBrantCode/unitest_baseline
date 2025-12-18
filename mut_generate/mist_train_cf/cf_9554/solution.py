"""
QUESTION:
Write a function `generate_subsets(elements)` that generates all possible non-empty subsets of a given set of elements in lexicographical order, without using any built-in functions or libraries for generating subsets. The function should take a list of elements as input and return a list of lists, where each sublist is a subset of the input list.
"""

def generate_subsets(elements):
    subsets = [[]]  
    elements.sort()  

    for element in elements:
        new_subsets = []  

        for subset in subsets:
            new_subset = subset + [element]  
            new_subsets.append(new_subset)

        subsets += new_subsets  

    return subsets