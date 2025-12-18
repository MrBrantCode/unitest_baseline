"""
QUESTION:
Write a function `find_furthest_elements(numbers)` that takes a list of real numbers as input and returns a tuple of the two numbers with the maximum spatial distance between them. The returned numbers should be in ascending order, and the input list must contain at least two elements.
"""

from typing import List, Tuple

def find_furthest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ Within a supplied list of real numbers having a compulsory minimum volume of two, decipher and generate the two constituents demonstrating the utmost numeric extent between them. The lower component should surface initially, trailed by the superior counterpart, while maintaining that the pairings are not chronologically ordered.
    """
    return (min(numbers), max(numbers))