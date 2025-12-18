"""
QUESTION:
Create a function called `rolling_min` that takes three lists of integers (`numbers1`, `numbers2`, `numbers3`) as input and returns a list of integers. The output list should contain the smallest element found up to the current point in the sequences, comparing corresponding elements from the input lists.

Restrictions: The input lists must be of the same length. The function should iterate over the input lists simultaneously, updating the minimal values found so far and appending the smallest of them to the output list.
"""

from typing import List

def rolling_min(numbers1: List[int], numbers2: List[int], numbers3: List[int]) -> List[int]:
    min_list = []
    min_values = [float('inf')] * 3
    for n1, n2, n3 in zip(numbers1, numbers2, numbers3):
        min_values[0] = min(min_values[0], n1)
        min_values[1] = min(min_values[1], n2)
        min_values[2] = min(min_values[2], n3)
        min_list.append(min(min_values))
        
    return min_list