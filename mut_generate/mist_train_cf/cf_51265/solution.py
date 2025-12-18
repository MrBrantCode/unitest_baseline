"""
QUESTION:
Write a function named `compute_product` that takes two lists of numbers as input and returns the sum of their pairwise products without using built-in functions like `sum()`, `prod()`, etc. The function should return an error message if the two input lists are not of equal length. The output should be a single number representing the sum of the pairwise products.
"""

def compute_product(list1, list2):
    if len(list1) != len(list2):
        return "Error: Both lists should be of the same length."
    else:
        zipped_lists = list(zip(list1, list2))
        result = 0
        for a, b in zipped_lists:
            result += a * b
        return result