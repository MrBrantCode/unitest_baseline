"""
QUESTION:
Extract all unique clusters of three elements from a supplied ordered collection of numerical data points. The function should take an ordered list of numbers as input and return a list of tuples, where each tuple is a cluster of three elements. The order of the elements in the clusters should be the same as in the original list.
"""

from itertools import combinations

def extract_clusters(data_points):
    """
    Extract all unique clusters of three elements from a supplied ordered collection of numerical data points.

    Args:
        data_points (list): An ordered list of numbers.

    Returns:
        list: A list of tuples, where each tuple is a cluster of three elements.
    """
    return list(combinations(data_points, 3))