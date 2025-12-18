"""
QUESTION:
Write a function `parallelogram_areas` that takes a list of pairs representing the base and height of parallelograms as input, where both base and height are integers between 1 and 10^6, and returns a list containing the corresponding areas of all the parallelograms. The function should have a time complexity of O(n), where n is the size of the input list.
"""

def parallelogram_areas(list_of_pairs):
    return [base*height for base, height in list_of_pairs]