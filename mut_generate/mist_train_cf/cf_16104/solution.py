"""
QUESTION:
Write a function `sum_first_last_elements` that takes a list of lists containing integers as input. For each inner list, the function should calculate the sum of the first and last elements and return these sums as a list of tuples, where each tuple contains the sum twice. The function should handle inner lists of any length and have a time complexity of O(n), where n is the total number of elements in the inner lists.
"""

def sum_first_last_elements(lst):
    result = []
    for inner_list in lst:
        first = inner_list[0]
        last = inner_list[-1]
        result.append((first + last, first + last))
    return result