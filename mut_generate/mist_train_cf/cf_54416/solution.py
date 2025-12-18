"""
QUESTION:
Find the median of n-dimensional tuple elements in a list without sorting the elements. The list can contain both even and odd numbers of elements. The function should be able to handle cases where the tuple number in the list is both even and odd. The function should take two parameters: n_dimension (the number of dimensions in the tuples) and lst (the list of n-dimensional integer tuples). The function should return the median of each dimension as an n-dimensional tuple.
"""

import statistics

def entrance(n_dimension: int, lst: list):
    """
    Finds and returns the median of n-dimensional tuple elements in the list lst without sorting the elements.
    The list can contain both even and odd numbers of elements.
    """
    medians = []
    # We transpose the list of tuples into a list of lists. The ith list in the result stores the ith element of all tuples.
    transposed_list = list(map(list, zip(*lst)))
    for i in range(n_dimension):
        medians.append(statistics.median(transposed_list[i]))
    return tuple(medians)