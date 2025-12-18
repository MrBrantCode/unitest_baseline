"""
QUESTION:
Implement the `weighted` and `subset` functions to select a subset of elements from a given list while maximizing the total weight without exceeding a specified limit. The functions should take a list of tuples representing elements and their weights, as well as a limit for the total weight, and return a list of tuples representing the selected subset of elements and their weights.

Assume that the `get(index: int) -> Tuple[Union[int, float], Union[int, float]]` function is already implemented to retrieve element weights and values. The `weighted` and `subset` functions should use this `get` function to access the weights and values of the elements.

The `weighted` function should have a time complexity of O(n), where n is the number of elements in the input list.
"""

from typing import List, Tuple, Union

def weighted(elements: List[Tuple[Union[int, float], Union[int, float]]], limit: Union[int, float]) -> List[Tuple[Union[int, float], Union[int, float]]]:
    selected_elements = []
    total_weight = 0
    for element in elements:
        value, weight = element
        if total_weight + weight <= limit:
            selected_elements.append((value, weight))
            total_weight += weight
    return selected_elements