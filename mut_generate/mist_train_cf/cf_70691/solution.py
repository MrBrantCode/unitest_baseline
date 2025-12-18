"""
QUESTION:
Create a function named `count_frequency_in_matrix` that takes an n-sized matrix as input and returns a dictionary with the frequency of each element in the matrix, handling both numerical and non-numerical elements, as well as nested lists. The function should be able to handle matrices with irregular structures and varying levels of nesting.
"""

def count_frequency_in_matrix(matrix):
    frequency_dict = {}
    for sublist in matrix:
        if isinstance(sublist, list):
            for item in sublist:
                if isinstance(item, list):
                    for subitem in item:
                        frequency_dict[subitem] = frequency_dict.get(subitem, 0) + 1
                else:
                    frequency_dict[item] = frequency_dict.get(item, 0) + 1
        else:
            frequency_dict[sublist] = frequency_dict.get(sublist, 0) + 1
    return frequency_dict