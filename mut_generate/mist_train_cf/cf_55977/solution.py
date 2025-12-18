"""
QUESTION:
Create a function find_furthest_elements that takes a list of numbers and returns a tuple of the two non-continuous elements with the greatest difference. The elements in the tuple should be in ascending order. The function should handle cases where the input list has less than two unique numbers.
"""

from typing import List, Tuple

def find_furthest_elements(numbers: List[float]) -> Tuple[float, float]:
    """ Identify and return the two discontinuous elements with the greatest difference from the given list of numbers. """

    # Filter out unique values, and sort the list in ascending order
    numbers = sorted(set(numbers))

    # If less than two unique numbers, return None
    if len(numbers) < 2:
        return None

    # Initialize variables assuming the first two are a valid pair
    max_diff = numbers[1] - numbers[0]
    max_pair = (numbers[0], numbers[1])

    # Iterate over the array to find the pair with the highest difference
    for i in range(len(numbers) - 2):
        diff = numbers[i + 2] - numbers[i]
        if diff > max_diff:
            max_diff = diff
            max_pair = (numbers[i], numbers[i + 2])
            
    return max_pair