"""
QUESTION:
Create a function `rolling_max_min(numbers)` that takes a list of integers and/or strings as input, filters out non-integer values, and returns a list of tuples representing the rolling maximum and minimum numbers observed in the list up to each point. The function should handle erroneous inputs, ignore duplicates, and return a list of tuples in the format (max, min).
"""

from typing import List, Union, Tuple

def rolling_max_min(numbers: List[Union[int, str]]) -> List[Tuple[int, int]]:
    """
    From a given numeral array or erroneous code, create a list of rolling maximum and minimum numbers observed 
    till a particular point in the array, represented as a tuple (max, min), ensuring there are no repeated 
    (max, min) tuples in the final list. The function should handle erroneous code inputs.
    """
    numbers = [n for n in numbers if isinstance(n, int)]  # Filter out non-int values
    if not numbers:
        return []

    rolling_min_max = [(numbers[0], numbers[0])]
    for num in numbers[1:]:
        current_max = max(num, rolling_min_max[-1][0])
        current_min = min(num, rolling_min_max[-1][1])
        if (current_max, current_min) != rolling_min_max[-1]:
            rolling_min_max.append((current_max, current_min))
            
    return rolling_min_max