"""
QUESTION:
Implement a function named `rolling_min` that takes two lists of integers `numbers1` and `numbers2` as input, and returns two lists containing the rolling minimum values from each list. The function should maintain the relative order of elements in the input lists, and at each index, the corresponding output should be the minimum value encountered up to that point in the respective list.
"""

from typing import List, Tuple

def rolling_min(numbers1: List[int], numbers2: List[int]) -> Tuple[List[int], List[int]]:
    """
    Using two given integer arrays as input, generate a series of rolling
    lowest components observed at any specific point in time in the sequence 
    and document them as the lowest value from each array.
    
    Args:
    numbers1 (List[int]): The first list of integers.
    numbers2 (List[int]): The second list of integers.

    Returns:
    Tuple[List[int], List[int]]: Two lists containing the rolling minimum values from each input list.
    """

    # Calculate rolling minimum for the first list
    min_values1 = [min(numbers1[:i+1]) for i in range(len(numbers1))]
    
    # Calculate rolling minimum for the second list
    min_values2 = [min(numbers2[:i+1]) for i in range(len(numbers2))]

    # Return the rolling minimum values for both lists
    return min_values1, min_values2