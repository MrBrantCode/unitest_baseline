"""
QUESTION:
Create a function named `generate_subsets` that takes a list of elements as input and returns a list of all possible non-empty subsets of the input list. The subsets should be generated in lexicographical order. The function should not use any built-in functions or libraries for generating subsets.
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